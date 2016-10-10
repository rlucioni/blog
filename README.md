# Pelican Site

This is the source for [my blog](https://renzo.lucioni.xyz/). It's generated using [Pelican](https://github.com/getpelican/pelican), a static site generator written in Python, in combination with a custom theme I created using Jinja2 templates and Sass. I've extended Pelican to do things like build a sitemap and link to related content at the end of posts.

## Getting Started

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
