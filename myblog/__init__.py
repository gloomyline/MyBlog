# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:20:31
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-31 17:12:53
import os
from flask import Flask, render_template, request
from flask_login import current_user
from myblog.settings import config
from myblog.models import Admin, Category, Post, Comment
from myblog.views.auth import auth_bp
from myblog.views.admin import admin_bp
from myblog.views.blog import blog_bp
from myblog.extensions import bootstrap, db, moment, ckeditor, mail, login_manager, csrf
from myblog.commands import register_commands
from flask_wtf.csrf import CSRFError

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('myblog')
    app.config.from_object(config[config_name])
    # register logger
    register_logging(app)
    # register extensions
    register_extensions(app)
    # blueprints register
    register_blueprints(app)
    # shell context
    register_shell_context(app)
    # template context
    register_template_context(app)
    # errors handle
    register_errors(app)
    # commands
    register_commands(app)
    return app


def register_logging(app):
    pass


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, Admin=Admin, Category=Category, Post=Post, Comment=Comment)


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        return dict(admin=admin, categories=categories)


def register_errors(app):
    @app.errorhandler(400)
    def bad_requests(e):
        return render_template('erros/400.html'), 400

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=u'会话过期或失效，请返回上一页面重试'), 400
