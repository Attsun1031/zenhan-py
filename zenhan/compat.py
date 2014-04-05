# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
import sys

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

if PY3:
    text_type = str
    unichr_ = chr
else:
    text_type = unicode
    unichr_ = unichr
