# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-09 18:01:30
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 13:14:25
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('board', instance_relative_config=True)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

moment = Moment(app)

toolbar = DebugToolbarExtension(app)

from board import views, commands
