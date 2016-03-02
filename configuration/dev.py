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
SITE_DESCRIPTION = "Renzo Lucioni's personal website and portfolio."
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

ARTICLE_ORDER_BY = 'reversed-date'
TYPOGRIFY = True

# Caching may interfere when experimenting with different settings, especially
# those related to metadata. If this occurs, use this to disable caching.
# LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True

##### URL settings #####
RELATIVE_URLS = False

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

##### Theming and Customization #####
THEME = 'themes/custom'

# Some of these might not be needed! Remove those which aren't used.
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'not_found', 'projects')

# GitHub Pages requires that custom 404 pages be accessible at the root
# level of a Pages repository as '404.html'.
NOT_FOUND_SAVE_AS = '404.html'

# A list of project metadata, used to generate the projects page
PROJECTS = [
    {
        'title': "Personal Website",
        'link': 'https://github.com/rlucioni/pelican-site',
        'project_id': 'pelican-site',
        # Dimensions should be 1000x600
        'image_filename': 'pelican-site.png',
        'description': "This is the source for the website you're currently visiting. It's a static site generated with Pelican.",
    },
    {
        'title': "Search Term Cards",
        'link': 'https://github.com/rlucioni/search-term-cards',
        'project_id': 'search-term-cards',
        'image_filename': 'search-term-card.png',
        'description': "This is a Flask app which displays site-search terms pulled from Google Analytics. It was inspired by and modeled after Google's own \"Hot Searches\" visualization. It's used to display popular search terms at edX's Cambridge office.",
    },
    {
        'title': "Yo Notifier",
        'link': 'https://github.com/rlucioni/yo-notifier',
        'project_id': 'yo-notifier',
        'image_filename': 'yo-notifier.png',
        'description': "This is a small Flask app which uses webhooks to send event-based Yo notifications. I use it to send push notifications to my phone.",
    },
    {
        'title': "Real-time Dashboard",
        'link': 'https://github.com/rlucioni/realtime-dashboard',
        'project_id': 'realtime-dashboard',
        'image_filename': 'pulse.gif',
        'description': "This is a Flask app which uses server-sent events to update a dashboard in real-time. I've used it to visualize registrations and enrollments on edX in real-time.",
    },
    {
        'title': "Project Euler Solutions",
        'link': 'https://github.com/rlucioni/project-euler',
        'project_id': 'project-euler',
        'image_filename': 'euler.png',
        'description': "This ongoing project includes my solutions to Project Euler problems, as well as a utility for timing the execution of solutions on different inputs.",
    },
]

PROJECTS_SAVE_AS = 'projects/index.html'

GITHUB_URL = 'https://github.com/rlucioni/'

# Whether InstantClick (https://github.com/dieulot/instantclick) should be used to preload pages
INSTANT_CLICK = True

# Whether FastClick (https://github.com/ftlabs/fastclick) should be used to remove click
# delays in browsers with touch UIs
FAST_CLICK = True

# These are dev keys. When a key is provided, the feature it corresponds to is enabled; to
# disable a feature, set its key to None.
GOOGLE_ANALYTICS_KEY = 'UA-33031883-4'
SEGMENT_KEY = 'KBYipO19jAaiwTxCCVkiD8MRcULFhAEz'

##### Plugins #####
PLUGIN_PATHS = ['../utilities']
PLUGINS = ['sitemap', 'related_posts']

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

RELATED_POSTS_MAX = 2
