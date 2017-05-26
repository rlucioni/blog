# Pelican Site

This is the source for [my blog](https://renzo.lucioni.xyz/). It's generated using Python 3.6 and [Pelican](https://github.com/getpelican/pelican), a static site generator, in combination with a custom theme I created using Jinja2 templates and Sass. I've extended Pelican to do things like build a sitemap and link to related content at the end of posts.

## Quickstart

Create a Python 3.6 virtualenv. You can do this with [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io). Source the virtualenv and install requirements:

```
$ make requirements
```

Build the site:

```
$ make
```

Serve the built site at http://localhost:8000 by running:

```
$ make serve
```

For information about additional Make targets:

```
$ make help
```

## Configuration

The site's settings module at `blog/settings.py` contains most of the Pelican configuration necessary to build the site. The `SITEURL` and `GOOGLE_ANALYTICS_KEY` settings can be overridden using environment variables.

## Deployment

Deployment to S3 is handled by [Travis](.travis.yml) on builds for the master branch. For more on this, see [this post](https://renzo.lucioni.xyz/s3-deployment-with-travis/).
