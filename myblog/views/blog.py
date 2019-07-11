# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:33:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-11 14:33:04
from flask import Blueprint, render_template
from myblog.models import Category, Post, Comment


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return render_template('views/index.html')


@blog_bp.route('/about')
def about():
    return render_template('views/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    return render_template('blog/category.html')


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    return render_template('blog/post.html')