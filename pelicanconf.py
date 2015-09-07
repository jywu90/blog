#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jingyao Wu/吴竞尧'
SITENAME = "Jingyao Wu's Blog"
SITEURL = 'http://jywu90.github.io/blog/'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
    #     ('Python.org', 'http://python.org/'),
   #      ('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)
#
# Social widget
SOCIAL = (('github', 'https://github.com/jywu90'),
          ('facebook', 'https://www.facebook.com/jingyao.wu.35'),
          ('500px', 'https://500px.com/JingyaoWu'),
           )

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/jingyao_wu/project/myblog/pelican-themes/Casper2Pelican"

# Content path.
PATH = 'content'
PAGE_DIR = 'pages'
# ARTICLE_DIR = 'articles'
# STATIC_PATHS = ['images', 'files']
# EXTRA_PATH_METADATA = {
#     'files/github/.nojekyll': {'path': '.nojekyll'},
#     'files/github/CNAME': {'path': 'CNAME'},
#     'files/github/404.html': {'path': '404.html'},
#     'files/github/README.md': {'path': 'README.md'},
#     'files/robots.txt': {'path': 'robots.txt'},
#     'images/favicon.ico': {'path': 'favicon.ico'},
# }

# URL settings
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
ARTICLE_URL = ('articles/{slug}/')
ARTICLE_SAVE_AS = ('articles/{slug}/index.html')
PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
AUTHOR_SAVE_AS = False