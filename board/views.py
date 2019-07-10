# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 08:56:40
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 10:15:42

from flask import flash, redirect, url_for, render_template

from board import app, db
from board.models import Message
from board.forms import HelloForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    # loading all of records
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        # create a Message model instance, create a new record
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)