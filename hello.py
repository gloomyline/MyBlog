import click
import os
from urllib.parse import urlparse, urljoin
from flask import Flask, request, abort, jsonify, make_response, redirect, \
    url_for, session, render_template
from forms import LoginForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret_key')
# upload file max size
# app.config[MAX_CONTENT_LENGTH] = 3 * 1024 * 1024


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))

def is_safe_url(target):
    host = request.host_url
    ref_url = urlparse(host)
    test_url = urlparse(urljoin(host, target))
    return test_url.schema in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='hello', **kwargs):
    """redirect back within default page hello"""
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


@app.route('/foo')
def foo():
    return '<h1>Foo page.</h1><a href="%s">do something</a>' % url_for('do_somethig', next=request.full_path)


@app.route('/bar')
def bar():
    return '<h1>Bar page.</h1><a href="%s">do something</a>' % url_for('do_somethig', next=request.full_path)

@app.route('/do-somenthing')
def do_somethig():
    return redirect_back()


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
@app.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
    if not post_id == post['id']:
        abort(404)
    else:
        return jsonify({'status': 200, 'message': 'ok', 'data': post})


@app.route('/post/<post_id>', methods=['POST'])
def edit_post(post_id):
    print(post_id)
    if not post_id == post['id']:
        return jsonify({'status': 401, 'message': 'this post is not existed', 'data': {}}), 401
    else:
        newPost = request.get_json()
        post['name'] = newPost['name']
        post['content'] = newPost['content']
        return jsonify({'status': 200, 'message': 'ok', 'data': {}})


# templates engine jinja2 example
@app.route('/')
def index():
    return render_template('index.html')


user = {
    'username': 'Alan Wang',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/watch-list')
def watch_list():
    return render_template('watchlist.html', user=user, movies=movies)


# forms
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        session['logged_in'] = True
        return redirect(url_for('hello'))
"""
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = uploadForm()
    return render_template('upload.html', form=form)
"""


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
