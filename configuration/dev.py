#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Settings used for development.

This file is consumed when running `make html`.
"""
from __future__ import unicode_literals

import os
from datetime import datetime


##### Basic settings #####
AUTHOR = "Renzo Lucioni"
SITENAME = "Renzo Lucioni"
SITE_DESCRIPTION = "Renzo Lucioni's personal website."
SITEURL = ''

LOCALE = 'en_US.UTF-8'
TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'
CURRENT_TIME = datetime.now()

PATH = 'content'
# Relative to PATH
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

# Directories (relative to PATH) in which to look for static files; these files
# will be copied to the output directory without modification.
STATIC_PATHS = [
    'images',
    'pdfs',
    'extra',
]

# Not all metadata needs to be embedded in a source file itself. This is a
# convenient way of modifying the installed location of particular files.
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Install all favicons at the root of the generated site; see
# http://realfavicongenerator.net/faq for more details.
for filename in os.listdir('content/images/favicons'):
    EXTRA_PATH_METADATA['images/favicons/' + filename] = {'path': filename}

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
ARCHIVES_SAVE_AS = ''
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

# A list of project metadata, used to generate the projects page
PROJECTS = [
    {
        'title': "Awesome Project",
        'link': 'http://www.reddit.com/',
        'image_path': 'http://placehold.it/800x400',
        'description': "This is my latest project. It is awesome.",
    },
    {
        'title': "A Sweet Project",
        'link': 'http://www.reddit.com/',
        'image_path': 'http://placehold.it/800x400',
        'description': "This is one of my later projects. It's pretty sweet!",
    },
    {
        'title': "First Project",
        'link': 'http://www.reddit.com/',
        'image_path': 'http://placehold.it/800x400',
        'description': "This was my first project. It was cool.",
    },
]

PROJECTS_SAVE_AS = 'projects/index.html'

GITHUB_URL = 'https://github.com/rlucioni/'

##### Plugins #####
PLUGIN_PATHS = ['../utilities']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'pages': 0.6,
        'indexes': 0.7,
    },
    'changefreqs': {
        'articles': 'weekly',
        'pages': 'weekly',
        'indexes': 'weekly',
    }
}
