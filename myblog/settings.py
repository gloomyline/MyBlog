# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-09 17:56:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 14:25:09

import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Alan\'s blog admin', MAIL_USERNAME)

    MYBLOG_EMAIL = os.getenv('MYBLOG_EMAIL')
    MYBLOG_POST_PER_PAGE = 10
    MYBLOG_MANAGE_POST_PER_PAGE = 15
    MYBLOG_COMMENT_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'splite:///' + os.path.join(basedir, 'data.db'))

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}