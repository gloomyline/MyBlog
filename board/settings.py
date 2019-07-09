# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-09 17:56:08
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-09 18:22:10

import os

from board import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)