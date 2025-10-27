---
title: Serverless Slack Bolt App
description: Building a serverless Slack app with Bolt, Flask, and Zappa
date: 2025-10-27T01:14:24-04:00
---

I was recently looking to build a Slack app using Slack's Bolt framework. I wanted to use Flask and host the app on AWS Lambda using [Zappa](https://github.com/zappa/Zappa). Slack's docs describe how to use Bolt's [adapters](https://docs.slack.dev/tools/bolt-python/concepts/adapters/) to make an app with Flask. They also show how to deploy a [JS Bolt app to AWS Lambda](https://docs.slack.dev/tools/bolt-js/deployments/aws-lambda/). Unfortunately, I had a hard time finding information about how to do this with Python, so I thought I'd write this up to help others interested in doing something similar.

The instructions for using Bolt with Flask might lead you to believe you can deploy an app like this:

```python
import os
import time

from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler


slack_app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

flask_app = Flask(__name__)
handler = SlackRequestHandler(slack_app)


@slack_app.event('app_mention')
def respond_to_mention(event):
    channel_id = event['channel']
    slack_app.client.chat_postMessage(
        channel=channel_id,
        text='Working on it...',
        thread_ts=event['ts']
    )

    # do some work
    time.sleep(1)

    slack_app.client.chat_postMessage(
        channel=channel_id,
        text='Done!',
        thread_ts=event['ts']
    )


@flask_app.route('/slack/events', methods=['POST'])
def slack_events():
    return handler.handle(request)
```

This will work as expected locally, but it won't when deployed to AWS Lambda. That's because Slack requires you to acknowledge event requests [within 3 seconds](https://docs.slack.dev/apis/events-api/#responding) and Bolt tries to help with this by automatically acknowledging requests. The problem is that it does this by sending an HTTP 200 response immediately. On FaaS runtimes like AWS Lambda, the execution context ends as soon as you return an HTTP response, so the logic in `respond_to_mention` doesn't get a chance to run.

Fortunately, there's an easy fix. Bolt provides a [`process_before_response`](https://docs.slack.dev/tools/bolt-python/concepts/lazy-listeners/) option you can pass when initializing your app. When enabled, Bolt waits to send its ack response until after your listener functions have run:

```python
slack_app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET'),
    process_before_response=True
)
```

The modified app will work as expected when deployed to AWS Lambda. Here's a bare-bones `zappa_settings.json` you can use to deploy it:

```json
{
  "prod": {
    "app_function": "app.flask_app",
    "exclude": [
      "zappa_settings.json"
    ],
    "keep_warm": true,
    "keep_warm_expression": "rate(5 minutes)",
    "memory_size": 512,
    "project_name": "example"
  }
}
```

These settings assume the app code above is in `app.py`, and a directory structure like:

```txt
example/
├── app.py
└── zappa_settings.json
```

The `keep_warm` settings tells Zappa to create recurring no-op CloudWatch events that keep your app function's execution environment available for reuse. This prevents the function from wasting valuable seconds [cold-starting](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html#cold-start-latency) (i.e., recreating the execution environment) and hitting Slack's 3-second timeout. A `memory_size` of 512 MB is the [sweet spot](https://medium.com/geekculture/pick-the-right-memory-size-for-your-aws-lambda-functions-682394aa4b21) between cost and performance.

You can deploy the app with:

```bash
$ zappa deploy prod
```

Check the status of your deployment with:

```bash
$ zappa status prod
```

And if you change the app code and want to update the deployed app:

```bash
$ zappa update prod
```

For a more complete example that also shows how to handle work that takes longer than 3 seconds to complete (e.g., generating content with an LLM), check out my [chefbot](https://github.com/rlucioni/recipes/tree/8eecb92914380f74884ccaeb2050e4c647f1431a/chefbot) project.
