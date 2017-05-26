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

IGNORE_FILES = [
    '.gitkeep',
    'sass',
]

PATH = 'blog/content'
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
    for filename in os.listdir(f'{PATH}/{directory}'):
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
THEME = 'blog/theme'

# TODO: Move projects and 404 pages here.
TEMPLATE_PAGES = {
    'resume.html': 'resume/index.html',
}

with open(f'{PATH}/resume.yml') as f:
    RESUME = yaml.load(f)['resume']

# Some of these might not be needed! Remove those which aren't used.
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'not_found', 'projects')

EXTRA_TEMPLATES_PATHS = [
    'blog/theme/static',
]

NOT_FOUND_SAVE_AS = '404.html'

with open(f'{PATH}/projects.yml') as f:
    PROJECTS = yaml.load(f)['projects']

PROJECTS_SAVE_AS = 'projects/index.html'

GITHUB_URL = 'https://github.com/rlucioni'

# This is a dev key. When a key is provided, pageview tracking to Google Analytics is enabled.
# To disable this, set the key to None.
GOOGLE_ANALYTICS_KEY = os.environ.get('GOOGLE_ANALYTICS_KEY', 'UA-33031883-4')

PLUGINS = [
    'blog.plugins.related_posts',
    'blog.plugins.sitemap',
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
