#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import os
import tempfile

temp = tempfile.TemporaryFile()
try:
    temp.write('Some data')
    temp.seek(0)
    
    print temp.read()
finally:
    temp.close()