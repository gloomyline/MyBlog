import click
from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, Flask!</h1>'


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Flask')
    return '<h1>Hello, %s!</h1>' % name


# customer defined command
@app.cli.command('say-hello')
def hello():
    """Just say hello!"""
    click.echo('Hello, man!')
