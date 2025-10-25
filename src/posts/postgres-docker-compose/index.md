---
title: Running Postgres with Docker Compose
description: How to run Postgres locally with Docker Compose
date: 2020-08-21T11:00:16-04:00
lastmod: 2020-08-21T11:00:16-04:00
---

Running [Postgres](https://www.postgresql.org) locally can be helpful during development, especially when working on an application that uses it in production. [Docker Compose](https://docs.docker.com/compose/install) makes it easy to do this quickly and consistently.

To follow along with my example below, create a file named `docker-compose.yml` and a directory adjacent to it named `postgres` containing one file, `postgres.conf`. Everything you need should be laid out like this:

```txt
docker-compose.yml
postgres/
  postgres.conf
```

Put the following in `docker-compose.yml`:

```yaml
version: "3.7"

services:
  postgres:
    image: "postgres:9.6"
    environment:
      POSTGRES_PASSWORD: "password"
    volumes:
      - "./postgres/postgres.conf:/usr/local/etc/postgres/postgres.conf"
      - "./postgres/data:/var/lib/postgresql/data:delegated"
    command: "postgres -c config_file=/usr/local/etc/postgres/postgres.conf"
    ports:
      - "5432:5432"
```

I'm using `postgres:9.6` in this example, but you can change that to any of the image tags listed in the official Postgres repo on [Docker Hub](https://hub.docker.com/_/postgres) (e.g., `postgres:10.14`). Avoid Alpine Linux images. They're tempting because they're so small, but they're also susceptible to confusing, image-specific [issues](https://github.com/docker-library/postgres/issues/327).

Use `POSTGRES_PASSWORD` to specify the password you want to use when connecting to the Postgres server. I'm using the very secure `password`, but you can change this, too.

`postgres/postgres.conf` is a Postgres [config file](https://github.com/postgres/postgres/blob/master/src/backend/utils/misc/postgresql.conf.sample). I'm mounting it as a volume so the container can read it when Postgres is started by `command`. To make the Postgres server listen for connections from clients on all available IP interfaces - useful when the server is running as a container and you want to connect to it from your host - put the following in your `postgres/postgres.conf`:

```txt
listen_addresses = '*'
```

`postgres/data/` is a directory that will be created on your host when you start Postgres. I'm mounting it as a volume to persist data written by the container, meaning that data written to Postgres will survive if the container is removed. The [`:delegated`](https://docs.docker.com/docker-for-mac/osxfs-caching/#delegated) suffix means that writes by the container to this volume may not be immediately reflected on the host file system (i.e., the container's view of the volume is authoritative). Delegating write-heavy mounts like this one reduces Docker's resource usage and gives you better performance than other [volume mount configurations](https://docs.docker.com/docker-for-mac/osxfs-caching/). Giving up some consistency guarantees like this is usually acceptable when working locally, especially when the data written is ephemeral or can be easily reproduced.

Finally, I'm mapping the default Postgres port 5432 to port 5432 on the host. Make sure nothing else is listening on port 5432 by running `lsof -i :5432`. It shouldn't return any output. If it does, shut down whatever's listening on 5432 (e.g., another Postgres server) or [bind to a different port](https://docs.docker.com/compose/compose-file/#short-syntax-1) on your host before proceeding.

You can now start a Postgres container in the background by running `docker-compose up -d`. This command will also pull the Postgres image specified in `docker-compose.yml` if it's not already present on your host. Check the status of the container by running `docker-compose ps`. Its `State` should be `Up` as shown below:

```txt
     Name                    Command               State           Ports
---------------------------------------------------------------------------------
blog_postgres_1   docker-entrypoint.sh postg ...   Up      0.0.0.0:5432->5432/tcp
```

You should now be able to connect to Postgres! For example, using [`psql`](https://www.postgresql.org/docs/9.6/app-psql.html):

```txt
psql -h localhost -p 5432 -U postgres
```

Remember to provide the value of `POSTGRES_PASSWORD` in `docker-compose.yml` when prompted for a password. You should then be connected to the server, at which point you can run commands like `\l` to list all databases and `\q` to quit `psql`.

```txt
psql (12.1, server 9.6.19)
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

postgres=# \q
```

That's it! You can pause the container by running `docker-compose pause`, resume it by running `docker-compose unpause`, and remove it by running `docker-compose down`.
