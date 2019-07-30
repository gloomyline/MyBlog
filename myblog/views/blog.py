# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:33:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-30 14:25:36
from flask import request, Blueprint, render_template, current_app, flash, redirect, url_for, make_response
from flask_login import current_user
from myblog.extensions import db
from myblog.models import Category, Post, Comment
from myblog.forms import AdminCommentForm, CommentForm
from myblog.emails import send_new_comment_email, send_new_reply_email
from myblog.utils import redirect_back

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
    form = None
    if current_user.is_authenticated: # current user is logined
        form = AdminCommentForm()
        form.author.data = current_user.name
        form.email.data = current_app.config['MYBLOG_EMAIL']
        form.site.data = url_for('.index')
        from_admin = True
        reviewed = True
    else: # not logined
        form = CommentForm()
        from_admin = False
        reviewed = True

    if form.validate_on_submit():
        author = form.author.data
        email = form.email.data
        site = form.site.data
        body = form.body.data
        comment = Comment(author=author, email=email, site=site, body=body,from_admin=from_admin, post=post, reviewed=reviewed)
        replied_id = request.args.get('reply')
        if replied_id:
            replied_comment = Comment.query.get_or_404(replied_id)
            comment.replied = replied_comment
            # send_new_reply_email(replied_comment)
        db.session.add(comment)
        db.session.commit()
        if current_user.is_authenticated:
            flash('Comment published', 'success')
        else:
            flash('Thanks, your comment will be published after reviewed.', 'info')
            # send_new_comment_email(post)
        return redirect(url_for('.show_post', post_id=post.id))

    return render_template('blog/post.html', post=post, comments=comments, form=form, pagination=pagination)


@blog_bp.route('/reply/comment/<int:comment_id>')
def reply_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if not comment.post.can_comment:
        flash('Comment is disabled.', 'warning')
        return redirect(url_for('.show_post', post_id=comment.post.id))
    return redirect(url_for('.show_post', post_id=comment.post_id, reply=comment_id, author=comment.author) + '#comment-form')


@blog_bp.route('/change-theme/<theme_name>')
def change_theme(theme_name):
    if theme_name not in current_app.config['MYBLOG_THEMES'].keys():
        abort(404)
    response = make_response(redirect_back())
    response.set_cookie('theme', theme_name, max_age=30*24*60*60)
    return response