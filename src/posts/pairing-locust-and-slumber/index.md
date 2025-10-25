---
title: Pairing Locust and Slumber
description: Elegant REST API load testing with Python, Locust, and Slumber.
date: 2015-10-01T21:51:28-04:00
lastmod: 2019-03-02T20:10:21-04:00
---

[Locust](https://github.com/locustio/locust) is a load testing tool written in Python. You can use it to better understand how many concurrent users a system can handle. [Slumber](https://github.com/samgiles/slumber) is a Python library that provides a nice object-oriented interface for consuming REST APIs. It's a wrapper around the Requests library that abstracts away URL handling, serialization, and request processing. I'll show you how the two can be combined to elegantly load test REST APIs.

Locust includes an extended version of Requests' `Session` class, [`HttpSession`](https://docs.locust.io/en/latest/api.html#httpsession-class). Locust relies on this class to log HTTP requests so that they'll appear in Locust's statistics reports. As such, Locust requires that instances of this class be used when making requests during load testing. Beyond logging request metadata, `HttpSession` augments the methods `Session` provides for making requests with an additional keyword argument, `name`. It can be used to group requests to URLs with dynamic parameters under a common name in Locust's statistics.

If you want to use Slumber in your load tests and still have your requests show up in Locust's statistics, you must provide an instance of `HttpSession`, accessible via the `client` attribute within a `TaskSet`, when constructing your API client.

```python
from locust import TaskSet, task
from slumber import API

class ExampleTaskSet(TaskSet):
    @task
    def example_task(self):
        url = 'http://example.com/api/v1/'
        api = API(url, session=self.client)

        # GET http://example.com/api/v1/resource/
        api.resource.get()
```

Taking full advantage of Locust's extensions requires overriding Slumber's `Resource` class. Doing so allows you to pass the `name` keyword argument mentioned above to Slumber's HTTP methods within the context of your tasks.

```python
import random

from locust import TaskSet, task
from slumber import Resource, API, exceptions

class LocustResource(Resource):
    def _request(self, method, data=None, files=None, params=None):
        serializer = self._store['serializer']
        url = self.url()

        headers = {'accept': serializer.get_content_type()}

        if not files:
            headers['content-type'] = serializer.get_content_type()
            if data is not None:
                data = serializer.dumps(data)

        # Used to group requests to URLs like
        #   'http://example.com/api/v1/resource/1/'
        # and
        #   'http://example.com/api/v1/resource/2/'
        # under a name like
        #   '/api/v1/resource/:id/'
        name = params.pop('name', None)

        resp = self._store['session'].request(
            method,
            url,
            data=data,
            params=params,
            files=files,
            headers=headers,
            name=name
        )

        if 400 <= resp.status_code <= 499:
            exception_class = exceptions.HttpNotFoundError if resp.status_code == 404 else exceptions.HttpClientError

            raise exception_class(
                'Client Error %s: %s' % (resp.status_code, url),
                response=resp,
                content=resp.content
            )
        elif 500 <= resp.status_code <= 599:
            raise exceptions.HttpServerError(
                'Server Error %s: %s' % (resp.status_code, url),
                response=resp,
                content=resp.content
            )

        self._ = resp

        return resp

class LocustApiClient(API):
    resource_class = LocustResource

class ExampleTaskSet(TaskSet):
    @task
    def example_task(self):
        url = 'http://example.com/api/v1/'
        api = LocustApiClient(url, session=self.client)

        # GET http://example.com/api/v1/resource/{id}/
        id = random.randint(1, 10)
        api.resource(id).get(name='foo')
```

The resulting requests will be listed in Locust's statistics under the name "foo."

With these modifications in hand, you can test your REST APIs using Locust without having to worry about URL manipulation or serialization. Happy load testing!
