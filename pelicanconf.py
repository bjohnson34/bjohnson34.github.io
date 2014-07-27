#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benjamin K Johnson'
SITENAME = u"Musings from the Ocean's Rim"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = '%A %d %B %Y'


# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


#Theme related stuff
THEME = 'notmyidea'

# Blogroll
LINKS = (('The Lab', 'http://abramovitchlab.com'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/BenJohnson3434'),
          ('Github', 'https://github.com/bjohnson34'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Contact
EMAIL_ADDR = 'john3434 at msu dot edu'
