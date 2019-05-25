import click
import os
from flask import Flask, request, abort, jsonify, make_response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret_key')


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Anny')
    response = '<h1>Hello, %s!</h1>' % name
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response


# URL variables transverter
@app.route('/welcome/<int:year>', methods=['GET', 'POST'])
def welcome(year):
    return 'Welcome to %d!' % (2019 - year)


colors = ['red', 'yellow', 'green']
@app.route('/color/<any(%s):color>' % str(colors)[1:-1])
def three_colors(color):
    return '<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.%s</p>' % color


# http, request, response
post = {
    'id': 'post001',
    'name': 'post1',
    'content': 'This is post1.'
}
@app.route('/foo/<post_id>', methods=['GET'])
def get_post(post_id):
    if not post_id == post['id']:
        abort(404)
    else:
        return jsonify({'status': 200, 'message': 'ok', 'data': post})


@app.route('/foo/<post_id>', methods=['POST'])
def edit_post(post_id):
    print(post_id)
    if not post_id == post['id']:
        return jsonify({'status': 401, 'message': 'this post is not existed', 'data': {}}), 401
    else:
        newPost = request.get_json()
        post['name'] = newPost['name']
        post['content'] = newPost['content']
        return jsonify({'status': 200, 'message': 'ok', 'data': {}})


# cookie
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response

@app.route('/brew/coffee')
def make_coffee():
    return 'The server is a teapot, not a coffee machine.', 418


@app.route('/404')
def not_found():
    abort(404)

# customer defined command
@app.cli.command('say-hello')
def hello():
    """Just say hello!"""
    click.echo('Hello, man!')
