Title: New Website
Description: Explaining the development process behind the new and improved renzolucioni.com.
Slug: new-website
Date: 2015-02-20 23:55
Modified: 2016-03-04 21:30
Author: Renzo Lucioni
Tags: pelican, website

I've spent the last two months working on a new static site with the intention of posting more regularly. My old site was built in a rush using tools I wasn't too comfortable with, namely Ruby, Jekyll, and Liquid templates.

This new site is generated using [Pelican](https://github.com/getpelican/pelican), a static site generator written in Python, in combination with a custom theme I created using Jinja2 templates and Sass. I'm more familiar with these tools than those used to build my old site. I've extended Pelican to do things like build a sitemap and link to related content at the end of posts.

Management commands used to develop and publish the site are `make` targets (EDIT: now [Invoke](https://github.com/pyinvoke/invoke) tasks), several built on top of the Pelican CLI. I prefer this approach to relying on the Jekyll CLI. Configuration details are stored in Python modules, which I prefer to the YAML settings file Jekyll depends on; I'm now able to have my production configuration inherit from a base set of development settings.

The site itself continues to be hosted on GitHub Pages. I attempt to reduce latency by using [InstantClick](https://github.com/dieulot/instantclick) to preload pages, as well as [FastClick](https://github.com/ftlabs/fastclick) to remove click delays in browsers with touch UIs. The new logo is a 529 byte SVG (!) I designed in [Sketch](http://bohemiancoding.com/sketch/), inspired by the work of [Tom Geismar](http://tomgeismar.com/). Images are all compressed using [TinyPNG](https://tinypng.com/).

The web fonts used by the site &ndash; Roboto and Fira Mono &ndash; were downloaded from Google Fonts. They are bundled with and served alongside the site to avoid fetching resources from third-party servers unnecessarily. Every favicon imaginable was generated with the help of [RealFaviconGenerator](http://realfavicongenerator.net/).

The source for the site is available on [GitHub](https://github.com/rlucioni/pelican-site). If this sounds like something you'd like to build for yourself, go for it! Let me know if you have questions.
