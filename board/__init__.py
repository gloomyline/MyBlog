# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-09 18:01:30
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-09 18:21:30
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('board')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

# from MyBlog import views, errors, commands