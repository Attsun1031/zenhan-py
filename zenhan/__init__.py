# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
import sys
from .compat import PY3, PY2

__version__ = '0.5.2'
ASCII = 1
DIGIT = 2
KANA  = 4
ALL = ASCII | DIGIT | KANA

if PY3 or PY2:
    from . import converter
    converter = converter.Converter()
else:
    sys.exit('Use Python 2 or 3')


def z2h(text, mode=ALL, ignore=()):
    return converter.zen2han(text, mode, ignore)

def h2z(text, mode=ALL, ignore=()):
    return converter.han2zen(text, mode, ignore)


