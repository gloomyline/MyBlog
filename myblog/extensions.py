# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:44:38
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 14:48:48
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
ckeditor =  CKEditor()