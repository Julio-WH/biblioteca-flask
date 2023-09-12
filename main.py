from flask import request, redirect, make_response, render_template, session
import unittest
from app import create_app, db

app = create_app()

# with app.app_context():
#     db.create_all()

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor ']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    contex = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username,
    }
    return render_template('hello.html', **contex)
