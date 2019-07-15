# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-15 10:12:47
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-15 10:16:26
import re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    '''Generates an ASCII-only slug.'''
    result = []
    for word in _punct_re.split(text.lower):
        result.extend(unidecode(word).lower().split())
    return unidecode(delim.join(result))