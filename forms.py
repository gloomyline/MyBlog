# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
# from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 16)])
    remember = BooleanField('Remember me')
    submit = SubmitField('log in')

class NewNoteForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Save')

class EditNoteForm(NewNoteForm):
    submit = SubmitField('Update')

class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')

"""
class UploadForm(FlaskForm):
    photo = FileField('Upload image', validators=[FileRequired(), FileAllowed('jpg', 'jpeg', 'png', 'gif')])
    submit = SubmitFiled()
"""
