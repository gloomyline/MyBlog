# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 15:37:47
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-30 18:49:24
from myblog.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_passwrod_hash(self.password_hash, password)


class User(Admin):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return AttributeError(u'该属性不可读')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    posts = db.relationship('Post', back_populates='category')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='posts')
    can_comment = db.Column(db.Boolean)
    comments = db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(254))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default=False)
    reviewed = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')
    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    replied = db.relationship('Comment', back_populates='replies', remote_side=[id])
    replies = db.relationship('Comment', back_populates='replied', cascade='all')
