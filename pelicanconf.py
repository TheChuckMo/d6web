#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chuck Mo'
SITENAME = 'D6Web'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('D6Engine Docs', 'https://docs.d6engine.org/'),
    ('D6Engine GitLab', 'https://gitlab.com/TheChuckMo/d6engine'),
    ('D6Dice Docs', 'https://d6dice.d6engine.org/'),
    ('D6Dice PyPi', 'https://pypi.org/projects/d6dice'),
    ('D6Dice GitLab', 'https://gitlab.com/TheChuckMo/d6dice'),
    ('OpenD6 System Reference', 'http: // opend6.wikidot.com /'),
)

# Social widget
SOCIAL = (('twitter/thechuckmo', 'https://twitter.com/thechuckmo'),)

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True