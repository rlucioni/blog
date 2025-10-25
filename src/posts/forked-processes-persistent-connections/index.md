---
title: Forked Processes and Persistent Connections
description: Working with persistent database connections across forked processes, or how to avoid sharing connections across child processes without breaking the parent's connection.
date: 2016-10-02T21:49:23-04:00
lastmod: 2019-03-02T20:10:21-04:00
---

I recently ran into problems working with forked processes sharing a database connection. In the process of figuring out what was wrong, I learned about how memory is managed during forking and how to avoid sharing connections across child processes without breaking the parent process' connection.

Persistent database connections avoid the overhead of having to repeatedly open connections to the database. They can improve the performance of your application, but they require special care if you're also working with forked processes.

Let's say you're using Django and the `ProcessPoolExecutor` from Python 3's [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) module. `ProcessPoolExecutor` uses the `multiprocessing` module, which forks processes when run on Unix-like operating systems. When `fork()` is called to create a new process, the Linux kernel applies the [copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write#Copy-on-write_in_virtual_memory_management) technique. Pages that the parent and child processes share, such as an open database connection, are marked as read-only. A shared page is only copied when a write such as closing the connection is performed, since the write means the memory shared by the two processes is no longer identical.

Depending on specifics of the driver and OS, the issues that arise from sharing database connections across processes range from non-working connections to socket connections that are used by multiple processes concurrently, leading to broken messaging. As such, a key goal when running multiple Python processes is to prevent any database connections from being shared. Closing an existing, copied connection as soon as a new child process is forked is an effective way of doing this, forcing each child process to open its own connection to the database. It works because as long as there is no existing, open connection, Django will initialize a new connection the next time one is necessary.

However, this approach can cause problems if the parent process needs to make any additional database queries. Calling `connection.close()` from a child process causes the database server to close a connection which the parent process thinks is still usable. This is due to the copy-on-write mechanic described above: the parent process' memory isn't updated when the child process modifies the connection state. Since the parent process thinks the connection is still open, Django won't attempt to open a new one. If the parent process needs to run additional queries, it will end up attempting to do so on a closed connection. This can result in errors like "MySQL server has gone away." To avoid this problem, reconnect the parent process to the database before running any queries.

Here's a pattern you can follow to maintain the parent process' connection while giving each child process its own connection.

```python
from concurrent.futures import ProcessPoolExecutor

from django.db import connection

from your.app.models import YourModel


def query():
    connection.close()
    YourModel.objects.exists()


for i in range(3):
    connection.connect()
    YourModel.objects.exists()

    with ProcessPoolExecutor() as executor:
        for j in range(3):
            executor.submit(query)
```
