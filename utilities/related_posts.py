# -*- coding: utf-8 -*-
"""A Pelican plugin for adding related posts to an article's context.

Adapted from http://goo.gl/8pq8MQ.
"""
from collections import Counter
from itertools import chain

from pelican import signals


def add_related_posts(generator):
    # Get the max number of entries from settings
    # or fall back to the default (5)
    numentries = generator.settings.get('RELATED_POSTS_MAX', 5)
    # Skip all posts in the same category as the article
    skipcategory = generator.settings.get('RELATED_POSTS_SKIP_SAME_CATEGORY', False)

    for article in generator.articles:
        # Set priority in case of forced related posts
        if hasattr(article, 'related_posts'):
            # Split slugs 
            related_posts = article.related_posts.split(',')
            posts = [] 

            # Get related articles
            for slug in related_posts:
                i = 0
                slug = slug.strip()
                for a in generator.articles:
                    if i >= numentries: # Break in case we've hit the max related posts
                        break
                    if a.slug == slug:
                        posts.append(a)
                        i += 1

            article.related_posts = posts
        else:
            # No tag, no relation
            if not hasattr(article, 'tags'):
                continue

            # Score is the number of common tags
            related = chain(*(generator.tags[tag] for tag in article.tags))
            if skipcategory:
                related = (other for other in related if other.category != article.category)
            scores = Counter(related)

            # Remove itself
            scores.pop(article, None)

            # Most_common sorts items with the same frequency in an arbitrary
            # order; it might be nice to sort related posts by date
            article.related_posts = [other for other, count in scores.most_common(numentries)]


def register():
    signals.article_generator_finalized.connect(add_related_posts)
