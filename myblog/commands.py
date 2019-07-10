# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 17:30:27
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 17:53:14
import click
from myblog.extensions import db
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