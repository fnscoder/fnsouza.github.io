#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Felipe N Souza'
SITENAME = 'FNScoder'
SITEURL = 'http://fnscoder.com/'
THEME = 'pelican-hyde'
PROFILE_IMAGE = 'avatar.jpg'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

BIO = 'Web developer'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'fnscoder@gmail.com'),
          ('github', 'https://github.com/fnscoder'),
          ('twitter', 'https://twitter.com/fnscoder'),
          ('linkedin', 'https://www.linkedin.com/in/fnscoder/'),
          ('file-text', 'https://drive.google.com/file/d/0B6M0onVHYLkyWGtzWW5pQVJLZzQ/view?usp=sharing'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extras/CNAME', 'extras/robots.txt']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
