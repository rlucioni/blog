from __future__ import unicode_literals

import os
from datetime import datetime


##### Basic settings #####
AUTHOR = 'Renzo Lucioni'
SITENAME = 'Renzo Lucioni'
SITE_DESCRIPTION = 'Renzo Lucioni\'s personal website and portfolio.'
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

# A list of project metadata, used to generate the projects page. Image dimensions should be 1000x600.
PROJECTS = [
    {
        'title': 'Rotations',
        'link': 'https://github.com/rlucioni/rotations',
        'description': 'Django app for managing rotations.',
    },
    {
        'title': 'Typesetter',
        'link': 'https://github.com/rlucioni/typesetter',
        'description': 'Flask and React application for help playing <a href="https://itunes.apple.com/us/app/letterpress-word-game/id526619424">Letterpress</a>.',
    },
    {
        'title': 'On This Day',
        'link': 'https://github.com/rlucioni/days',
        'description': 'Django application for learning about notable historical events.',
    },
    {
        'title': 'Personal Website',
        'link': 'https://github.com/rlucioni/blog',
        'description': 'The source for the website you\'re currently visiting. A static site generated with Pelican.',
    },
    {
        'title': 'Search Term Cards',
        'link': 'https://github.com/rlucioni/search-term-cards',
        'description': 'Flask app which displays site-search terms pulled from Google Analytics. Inspired by and modeled after Google\'s own "Hot Searches" visualization. It\'s been used to display popular search terms at edX\'s Cambridge office.',
    },
    {
        'title': 'Yo Notifier',
        'link': 'https://github.com/rlucioni/yo-notifier',
        'description': 'Flask app which uses webhooks to send event-based Yo notifications. I\'ve used it to send push notifications to my phone.',
    },
    {
        'title': 'Real-time Dashboard',
        'link': 'https://github.com/rlucioni/realtime-dashboard',
        'description': 'Flask app which uses server-sent events to update a dashboard in real-time. I\'ve used it to visualize registrations and enrollments on edX in real-time.',
    },
    {
        'title': 'Project Euler',
        'link': 'https://github.com/rlucioni/project-euler',
        'description': 'My solutions to Project Euler problems, written in Python.',
    },
]

PROJECTS_SAVE_AS = 'projects/index.html'

GITHUB_URL = 'https://github.com/rlucioni/'

# This is a dev key. When a key is provided, pageview tracking to Google Analytics is enabled.
# To disable this, set the key to None.
GOOGLE_ANALYTICS_KEY = 'UA-33031883-4'

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
