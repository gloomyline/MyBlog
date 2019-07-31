# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:44:38
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-31 17:03:49
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
ckeditor =  CKEditor()
login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from myblog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'warning'
