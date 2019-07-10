# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:32:59
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 15:21:29
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    pass


@auth_bp.route('/logout')
def logout():
    pass