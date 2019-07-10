# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:33:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 15:32:30
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return '<p>Hello!</p>'