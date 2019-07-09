# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
# from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 16)])
    remember = BooleanField('Remember me')
    submit = SubmitField('log in')


"""
class UploadForm(FlaskForm):
    photo = FileField('Upload image', validators=[FileRequired(), FileAllowed('jpg', 'jpeg', 'png', 'gif')])
    submit = SubmitFiled()
"""
