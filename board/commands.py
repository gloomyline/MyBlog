# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 09:57:16
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 10:07:05

import click
from faker import Faker
from board import app, db
from board.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the database.'''
    if drop:
        click.confirm('This operation will delete the database, do you wanna continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables')
    db.create_all()
    click.echo('Initialized database.')



@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    '''Generate fake messages.'''
    db.drop_all()
    db.create_all()
    fake = Faker()
    click.echo('Working...')
    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('Created %d fake messages' % count)
