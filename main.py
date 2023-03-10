from flask import request, make_response, redirect, render_template, session
import unittest
from app import create_app
app = create_app() 

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_id'] = user_ip
    return response

@app.route('/hello', methods=['GET'])
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username,
    }

    return render_template('hello.html', **context)