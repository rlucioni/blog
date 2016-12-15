# Pelican Site

This is the source for [my blog](https://renzo.lucioni.xyz/). It's generated using Python 3 and [Pelican](https://github.com/getpelican/pelican), a static site generator, in combination with a custom theme I created using Jinja2 templates and Sass. I've extended Pelican to do things like build a sitemap and link to related content at the end of posts.

## Getting Started

Create a Python 3 virtualenv. If you're using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io), you can do this with:

```
$ mkvirtualenv blog --python=$(which python3)
```

Source the virtualenv and install requirements:

```
$ workon blog
(blog)$ pip install -r requirements.txt
```

[Invoke](https://github.com/pyinvoke/invoke) tasks are used to develop and publish the site. Invoke configuration is stored in `invoke.yaml`. List all available tasks by running:

```
$ inv -l
```

Create a new draft post and open it for editing by running:

```
$ inv post -t <title> -d <description>
```

A slug for the new post is automatically generated from the provided title.

Serve the site and watch for changes, refreshing the site *and the browser* when changes are detected by running:

```
$ inv stream
```

## Configuration

The site's settings module, `settings.py`, contains most of the Pelican config necessary to build the site. The `SITEURL` and `GOOGLE_ANALYTICS_KEY` settings can be overridden using environment variables.

## Deployment

Deployment to S3 is handled by Travis on builds for the master branch.
