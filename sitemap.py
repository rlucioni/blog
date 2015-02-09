# -*- coding: utf-8 -*-
"""A Pelican plugin for generating plain-text or XML sitemaps.

Adapted from http://goo.gl/uFLE9I.
"""

from __future__ import unicode_literals

import collections
import os.path
from datetime import datetime
from logging import warning, info
from codecs import open
from pytz import timezone

from pelican import signals, contents
from pelican.utils import get_date


TXT_HEADER = """{0}/index.html
{0}/archives.html
{0}/tags.html
{0}/categories.html
"""

XML_HEADER = """<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

XML_URL = """
<url>
<loc>{0}/{1}</loc>
<lastmod>{2}</lastmod>
<changefreq>{3}</changefreq>
<priority>{4}</priority>
</url>
"""

XML_FOOTER = """
</urlset>
"""


def format_date(date):
    # For context, refer to http://www.w3.org/TR/NOTE-datetime.
    if date.tzinfo:
        tz = date.strftime('%z')
        tz = tz[:-2] + ':' + tz[-2:]
    else:
        tz = "-05:00"
    return date.strftime("%Y-%m-%dT%H:%M:%S") + tz


class SitemapGenerator(object):
    """Sitemap generator, to be subscribed to Pelican's get_generators signal."""
    def __init__(self, context, settings, path, theme, output_path, *null):
        self.output_path = output_path
        self.context = context
        self.now = datetime.now()
        self.siteurl = settings.get('SITEURL')

        self.default_timezone = settings.get('TIMEZONE', 'UTC')
        self.timezone = getattr(self, 'timezone', self.default_timezone)
        self.timezone = timezone(self.timezone)

        self.format = 'xml'

        self.changefreqs = {
            'articles': 'monthly',
            'pages': 'monthly',
            'indexes': 'daily',
        }

        self.priorities = {
            'articles': 0.5,
            'pages': 0.5,
            'indexes': 0.5,
        }

        config = settings.get('SITEMAP', {})

        if not isinstance(config, dict):
            warning("Sitemap plugin: the SITEMAP setting must be a dict")
        else:
            fmt = config.get('format')
            pris = config.get('priorities')
            chfreqs = config.get('changefreqs')

            if fmt not in ('xml', 'txt'):
                warning("Sitemap plugin: SITEMAP['format'] must be `txt' or `xml'")
                warning("Sitemap plugin: Setting SITEMAP['format'] on `xml'")
            elif fmt == 'txt':
                self.format = fmt
                return

            valid_keys = ('articles', 'indexes', 'pages')
            valid_chfreqs = ('always', 'hourly', 'daily', 'weekly', 'monthly',
                    'yearly', 'never')

            if isinstance(pris, dict):
                # We use items for Py3k compat. .iteritems() otherwise
                for k, v in pris.items():
                    if k in valid_keys and not isinstance(v, (int, float)):
                        default = self.priorities[k]
                        warning("Sitemap plugin: priorities must be numbers")
                        warning("Sitemap plugin: setting SITEMAP['priorities']"
                                "['{0}'] on {1}".format(k, default))
                        pris[k] = default
                self.priorities.update(pris)
            elif pris is not None:
                warning("Sitemap plugin: SITEMAP['priorities'] must be a dict")
                warning("Sitemap plugin: using the default values")

            if isinstance(chfreqs, dict):
                # .items() for py3k compat.
                for k, v in chfreqs.items():
                    if k in valid_keys and v not in valid_chfreqs:
                        default = self.changefreqs[k]
                        warning("Sitemap plugin: invalid changefreq `{0}'".format(v))
                        warning("Sitemap plugin: setting SITEMAP['changefreqs']"
                                "['{0}'] on '{1}'".format(k, default))
                        chfreqs[k] = default
                self.changefreqs.update(chfreqs)
            elif chfreqs is not None:
                warning("Sitemap plugin: SITEMAP['changefreqs'] must be a dict")
                warning("Sitemap plugin: using the default values")

    def write_url(self, page, fd):
        # Don't include the 404 page in the sitemap
        if page.url == 'not_found.html':
            return

        if getattr(page, 'status', 'published') != 'published':
            return

        # We can disable categories/authors/etc by using False instead of ''
        if not page.save_as:
            return

        page_path = os.path.join(self.output_path, page.save_as)
        if not os.path.exists(page_path):
            return

        lastdate = getattr(page, 'date', self.now)
        try:
            lastdate = self.get_date_modified(page, lastdate)
        except ValueError:
            warning("Sitemap plugin: " + page.save_as + " has invalid modification date,")
            warning("Sitemap plugin: using date value as lastmod.")
        lastmod = format_date(lastdate)

        if isinstance(page, contents.Article):
            pri = self.priorities['articles']
            chfreq = self.changefreqs['articles']
        elif isinstance(page, contents.Page):
            pri = self.priorities['pages']
            chfreq = self.changefreqs['pages']
        else:
            pri = self.priorities['indexes']
            chfreq = self.changefreqs['indexes']

        pageurl = page.save_as.replace('index.html', '')

        if self.format == 'xml':
            fd.write(XML_URL.format(self.siteurl, pageurl, lastmod, chfreq, pri))
        else:
            fd.write(self.siteurl + '/' + pageurl + '\n')

    def get_date_modified(self, page, default):
        if hasattr(page, 'modified'):
            if isinstance(page.modified, datetime):
                return page.modified
            return get_date(page.modified)
        else:
            return default

    def set_url_wrappers_modification_date(self, wrappers):
        for (wrapper, articles) in wrappers:
            lastmod = datetime.min.replace(tzinfo=self.timezone)
            for article in articles:
                lastmod = max(lastmod, article.date.replace(tzinfo=self.timezone))
                try:
                    modified = self.get_date_modified(article, datetime.min).replace(tzinfo=self.timezone)
                    lastmod = max(lastmod, modified)
                except ValueError:
                    # Supressed: user will be notified.
                    pass
            setattr(wrapper, 'modified', str(lastmod))

    def generate_output(self, writer):
        path = os.path.join(self.output_path, 'sitemap.{0}'.format(self.format))

        pages = self.context['pages'] + self.context['articles'] \
                + [ c for (c, a) in self.context['categories']] \
                + [ t for (t, a) in self.context['tags']] \
                + [ a for (a, b) in self.context['authors']]

        self.set_url_wrappers_modification_date(self.context['categories'])
        self.set_url_wrappers_modification_date(self.context['tags'])
        self.set_url_wrappers_modification_date(self.context['authors'])

        for article in self.context['articles']:
            pages += article.translations

        info('writing {0}'.format(path))

        with open(path, 'w', encoding='utf-8') as fd:

            if self.format == 'xml':
                fd.write(XML_HEADER)
            else:
                fd.write(TXT_HEADER.format(self.siteurl))

            DirectTemplatePage = collections.namedtuple(
                'DirectTemplatePage',
                ['status', 'date', 'url', 'save_as']
            )

            for slug in self.context['DIRECT_TEMPLATES']:
                direct_template_page = DirectTemplatePage(
                    status='published',
                    date=self.now,
                    url=slug + '.html',
                    save_as=self.context.get(slug.upper() + '_SAVE_AS', slug + '.html')
                )
                self.write_url(direct_template_page, fd)

            for page in pages:
                self.write_url(page, fd)

            if self.format == 'xml':
                fd.write(XML_FOOTER)


def get_generators(generators):
    return SitemapGenerator


def register():
    signals.get_generators.connect(get_generators)
