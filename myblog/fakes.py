# -*- coding: utf-8 -*-
# @comment:             data mock helpers
# @Author:              AlanWang
# @Date:                2019-07-10 16:42:58
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-15 16:11:25
import random

from faker import Faker
from myblog.models import Admin, Category, Post, Comment
from myblog.extensions import db

# argument 'zh_CN' is for Chinese
fake = Faker('zh_CN')


def fake_admin():
    admin = Admin(username='Admin',
        blog_title='myblog',
        blog_sub_title='No, I\'m the real thing.',
        name='Alan Wang',
        about='lazy to leave anythings~'
    )
    admin.set_password('@123456')
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    category = Category(name='Default')
    db.session.add(category)

    for i in range(count):
        _category = Category(name=fake.word())
        db.session.add(_category)
        try:
            db.session.commit()
        except InterityError:
            db.session.rollback()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.word(),
            body=fake.text(),
            timestamp=fake.date_time_this_year(),
            category=Category.query.get(random.randint(1, Category.query.count())),
            can_comment=random.randint(0, 1) > 0,
        )
        db.session.add(post)
    db.session.commit()

def fake_comments(count=500):
    salt = int(count * 0.1)
    for i in range(count):
        reviewed_comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(reviewed_comment)
    for i in range(salt):
        # comments which are not reviewed
        not_reviewed_comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(not_reviewed_comment)
    db.session.commit()
    # comments from admin
    comment = Comment(
        author='Alan Wang',
        email='alan@example.com',
        site='example.com',
        body=fake.sentence(),
        timestamp=fake.date_time_this_year(),
        reviewed=True,
        post=Post.query.get(random.randint(1, Post.query.count()))
    )
    db.session.add(comment)
    db.session.commit()
    # replies
    for i in range(salt):
        replied_comment=Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count())),
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
        )
        db.session.add(replied_comment)
    db.session.commit()
