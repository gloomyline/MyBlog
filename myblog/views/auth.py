# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 14:32:59
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-31 11:45:25
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from myblog.models import Admin
from myblog.forms import LoginForm
from myblog.utils import redirect_back

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    pass