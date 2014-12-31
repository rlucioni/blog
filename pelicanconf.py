#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Settings used for development.

This file is consumed when running `make html`.
"""

from __future__ import unicode_literals


##### Basic settings #####
AUTHOR = 'Renzo Lucioni'
SITENAME = 'renzolucioni.com'
SITEURL = ''

LOCALE = 'en_US.UTF-8'
TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'

PATH = 'content'
# Relative to PATH
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

# Directories (relative to PATH) in which to look for static files; these files
# will be copied to the output directory without modification.
STATIC_PATHS = [
    # 'images',
    # 'pdfs',
    'extra/CNAME',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/404.html',
]

# Not all metadata needs to be embedded in a source file itself. This is a
# convenient way of modifying the installed location of particular files.
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    # GitHub Pages requires that custom 404 pages be accessible at the root
    # level of a Pages repository as '404.html'. If I were to place a '404.md'
    # file in the 'pages' directory, the approach for creating clean URLs
    # suggested by the official Pelican docs would only allow access to the 404
    # page at '/404', not '/404.html' as required by GitHub Pages. Since GitHub
    # Pages doesn't support server configuration files like '.htaccess', this is
    # a functioning (but not ideal) workaround.
    'extra/404.html': {'path': '404.html'},
}

ARTICLE_ORDER_BY = 'date'
TYPOGRIFY = True

# Caching may interfere when experimenting with different settings, especially
# those related to metadata. If this occurs, use this to disable caching.
# LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True

##### URL settings #####
RELATIVE_URLS = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# This site only has one author, so we don't need an Authors page
AUTHOR_SAVE_AS = ''

##### Feed settings #####
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

##### Pagination #####
DEFAULT_PAGINATION = 5

##### I18N #####
TRANSLATION_FEED_ATOM = None

##### Theming #####
# THEME = 'simple'
GITHUB_URL = 'https://github.com/rlucioni/'
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

##### Plugins #####
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'pages': 0.5,
        'indexes': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'monthly',
        'indexes': 'daily'
    }
}
