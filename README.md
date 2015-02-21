This is the source for a static site generated with [Pelican](http://blog.getpelican.com/). It will eventually be served at [www.renzolucioni.com](http://www.renzolucioni.com/).


### Working with `make` ###

To generate the site's CSS, run `make css`. This processes the included Sass files and outputs minified CSS.

To generate the site's HTML, run `make html`. This invokes Pelican, which uses the settings defined in `configuration/dev.py` and the included Jinja2 templates to produce the site's static pages.

To serve the site at `http://localhost:8000`, run `make serve`.

To perform all three steps, run `make fresh`.


### Configuring for Production ###

To configure the site for production, create a file for the target production environment in `configuration/`. My site is hosted on GitHub Pages, and my configuration is at `configuration/github.py`. This file is consumed when running `make publish`, and should be used to import and override values from `configuration/dev.py`. At a minimum, the file should contain something like the following:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys

# https://github.com/getpelican/pelican/issues/406
sys.path.append(os.curdir)

from configuration.dev import *


SITEURL = 'http://www.renzolucioni.com'
DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = False
```
