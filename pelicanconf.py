#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Settings used for development.

This file is consumed when running `make html`.
"""

from __future__ import unicode_literals
import datetime


##### Basic settings #####
AUTHOR = 'Renzo Lucioni'
SITENAME = 'Site Name'
SITE_DESCRIPTION = 'Site description goes here.'
SITEURL = ''

LOCALE = 'en_US.UTF-8'
TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'
CURRENT_TIME = datetime.datetime.now()

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
]

# Not all metadata needs to be embedded in a source file itself. This is a
# convenient way of modifying the installed location of particular files.
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
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

# Prevent some default pages from being created
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

##### Feed settings #####
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

##### Pagination #####
DEFAULT_PAGINATION = False

##### I18N #####
TRANSLATION_FEED_ATOM = None

##### Theming #####
THEME = 'themes/custom'

# Some of these might not be needed! Remove those which aren't used.
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'not_found', 'projects')

# GitHub Pages requires that custom 404 pages be accessible at the root
# level of a Pages repository as '404.html'.
NOT_FOUND_SAVE_AS = '404.html'

PROJECTS_SAVE_AS = 'projects/index.html'

GITHUB_URL = 'https://github.com/rlucioni/'

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
