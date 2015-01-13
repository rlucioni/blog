renzolucioni.com
================

This is the source for a static site generated with [Pelican](http://blog.getpelican.com/).

Before building the site, you'll need to clone [`pelican-plugins`](https://github.com/getpelican/pelican-plugins). I keep it in a directory adjacent to `pelican-site`.

To generate the site's CSS, run `make style`. This processes the included Sass files and outputs minified CSS.

To generate the site's HTML, run `make html`. This invokes pelican, which uses the settings defined in `pelicanconf.py` and the included Jinja2 templates to produce the site's static pages.
