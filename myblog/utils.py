# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-15 10:12:47
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-30 14:30:22
import re
from unidecode import unidecode
from flask import request, redirect, url_for, current_app
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    '''Generates an ASCII-only slug.'''
    result = []
    for word in _punct_re.split(text.lower):
        result.extend(unidecode(word).lower().split())
    return unidecode(delim.join(result))

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))