# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:33:16
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-31 16:58:42
from flask import Blueprint
from flask_login import login_required

admin_bp = Blueprint('admin', __name__)

# 为所有的仕途函数添加登录保护
@admin_bp.before_request
@login_required
def login_protect():
    pass