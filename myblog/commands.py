# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 17:30:27
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-31 09:21:37
import click
from myblog.extensions import db
from myblog.models import Admin, Category
from myblog.fakes import fake_admin, fake_categories, fake_comments, fake_posts


def register_commands(app):
    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    @click.option('--comment', default=500, help='Quantity of comments, default is 500.')
    def forge(category, post, comment):
        '''Generates the fake categories, posts and comments.'''
        db.drop_all()
        db.create_all()
        click.echo('Generating the administrator...')
        fake_admin()
        click.echo('Generating %d categories' % category)
        fake_categories(category)
        click.echo('Generating %d posts' % post)
        fake_posts(post)
        click.echo('Generating %d comments' % comment)
        fake_comments(comment)
        click.echo('done.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True)
    def init(username, password):
        """Building MyBlog, just for you."""
        click.echo('Initializing the database...')
        db.create_all()

        admin = Admin.query.first()
        if admin: # 如果数据库中已经有管理员记录就更新用户和密码
            click.echo('The administrator already exsists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(
                username=username,
                blog_title='MyBlog',
                blog_sub_title="Discover the beauty everywhere.",
                name='Admin',
                about='Some things about you'
            )
            admin.set_password(password)
            db.session.add(admin)

            category = Category.query.first()
            if category is None:
                click.echo('Creating the default category...')
                category = Category(name='default')
                db.session.add(category)

            db.session.commit()
            click.echo('Done.')
