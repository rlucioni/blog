import datetime
import os

import yaml


with open('invoke.yaml') as f:
    data = yaml.load(f)


##### Basic settings #####
AUTHOR = data['author']
SITENAME = data['author']
SITE_DESCRIPTION = 'Renzo Lucioni\'s personal website and portfolio.'
SITEURL = os.environ.get('SITEURL', '')

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
    'images',
    'pdfs',
    'extra',
]

# Modify the installed location of particular files.
# Will install "extra" files and favicons at the root of the generated site.
# See http://realfavicongenerator.net/faq for more details.
EXTRA_PATH_METADATA = {}
for directory in ('extra', 'images/favicons'):
    for filename in os.listdir('content/' + directory):
        EXTRA_PATH_METADATA['{}/{}'.format(directory, filename)] = {'path': filename}

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

NOT_FOUND_SAVE_AS = '404.html'

# TODO: Move to YAML.
# A list of project metadata, used to generate the projects page.
PROJECTS = [
    {
        'title': 'Planet Money Complete',
        'link': 'https://github.com/rlucioni/pmoney',
        'description': 'An exploration of Planet Money\'s complete catalog.',
    },
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
        'description': 'Source for my personal website, https://renzo.lucioni.xyz. A static site generated with Pelican.',
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
GOOGLE_ANALYTICS_KEY = os.environ.get('GOOGLE_ANALYTICS_KEY', 'UA-33031883-4')

PLUGINS = [
    'plugins.related_posts',
    'plugins.sitemap',
]

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
