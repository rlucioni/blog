#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Settings used in production.

This file is consumed when running `make publish`. It imports and overrides
values from pelicanconf.
"""

from __future__ import unicode_literals

import os
import sys

# https://github.com/getpelican/pelican/issues/406
sys.path.append(os.curdir)

from pelicanconf import *


##### Basic settings #####
SITEURL = 'http://blog.renzolucioni.com'
DELETE_OUTPUT_DIRECTORY = True

##### URL settings #####
RELATIVE_URLS = False

##### Theming #####
# GOOGLE_ANALYTICS = ''
