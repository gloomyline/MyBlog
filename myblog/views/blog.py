# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:33:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-11 09:01:44
import json
import random
from flask import Blueprint
from myblog.models import Category, Post, Comment


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return '<p>Hello!</p>'


@blog_bp.route('/posts')
def fetch_posts():
    return Post.query.get(random.randint(1, Post.query.count())).body