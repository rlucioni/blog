# Pelican Site

This is the source for my personal site, [www.renzolucioni.com](http://www.renzolucioni.com/). It's generated using [Pelican](https://github.com/getpelican/pelican), a static site generator written in Python, in combination with a custom theme I created using Jinja2 templates and Sass. I've extended Pelican to do things like build a sitemap and link to related content at the end of posts.

## Getting Started

[Invoke](https://github.com/pyinvoke/invoke) tasks are used to develop and publish the site. Invoke configuration is stored in `invoke.yaml`. List all available tasks by running:

```
$ invoke --list
```

Create a new draft post and open it for editing by running:

```
$ invoke post -t <title> -d <description>
```

A slug for the new post is automatically generated from the provided title.

Serve the site and watch for changes, refreshing the site *and the browser* when changes are detected by running:

```
$ invoke stream
```

Generate the site using production settings and publish it to GitHub Pages by running:

```
$ invoke publish
```

## Configuration

Site configuration is stored in Python modules. Production configuration modules override the contents of a base development configuration module.

To configure the site for production, create a file for the target production environment in the `configuration` directory. My site is hosted on GitHub Pages, and my private configuration is at `configuration/github.py`. This module is consumed when running `invoke publish`.

Production settings modules should import and override values from `configuration/dev.py`. At a minimum, these modules should contain something like the following:

```python
from __future__ import unicode_literals

import os
import sys

# https://github.com/getpelican/pelican/issues/406
sys.path.append(os.curdir)

from configuration.dev import *


SITEURL = 'http://www.renzolucioni.com'
GOOGLE_ANALYTICS_KEY = 'YOUR GOOGLE ANALYTICS KEY'
SEGMENT_KEY = 'YOUR SEGMENT KEY'
```

## Performance

My site is hosted on GitHub Pages. I've attempted to reduce latency by using [InstantClick](https://github.com/dieulot/instantclick) to preload pages, as well as [FastClick](https://github.com/ftlabs/fastclick) to remove click delays in browsers with touch UIs.

My logo is a 529 byte SVG which I designed in [Sketch](http://bohemiancoding.com/sketch/), inspired by the work of [Tom Geismar](http://tomgeismar.com/). Images are all compressed using [TinyPNG](https://tinypng.com/).

The web fonts used by the site &ndash; Roboto and Fira Mono &ndash; were downloaded from Google Fonts. They are bundled with and served alongside the site to avoid fetching resources from third-party servers unnecessarily. Every favicon imaginable was generated with the help of [RealFaviconGenerator](http://realfavicongenerator.net/).
