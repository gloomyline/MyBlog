# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 08:52:09
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 10:12:29

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()