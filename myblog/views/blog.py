# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:33:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-15 14:21:56
from flask import request, Blueprint, render_template, current_app
from myblog.models import Category, Post, Comment

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/', defaults={'page': 1})
@blog_bp.route('/page/<int:page>')
def index(page):
    per_page = current_app.config['MYBLOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page, error_out=True)
    posts = pagination.items
    return render_template('blog/index.html', posts=posts, pagination=pagination)


@blog_bp.route('/about')
def about():
    return render_template('about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    per_page = current_app.config['MYBLOG_POST_PER_PAGE']
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.with_parent(category).order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/category.html', category=category, posts=posts, pagination=pagination)


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    per_page = current_app.config['MYBLOG_POST_PER_PAGE']
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.with_parent(post).filter_by(reviewed=True).order_by(Comment.timestamp.desc()).paginate(page, per_page=per_page)
    comments = pagination.items
    return render_template('blog/post.html', post=post, comments=comments, pagination=pagination)


@blog_bp.route('/reply/comment/<int:comment_id>')
def reply_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if not comment.post.can_comment:
        flash('Comment is disabled.', 'warning')
        return redirect(url_for('.show_post', post_id=comment.post.id))
    return redirect(url_for('.show_post', post_id=comment.post_id, reply=comment_id, author=comment.author) + '#comment-form')