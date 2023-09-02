from flask import render_template, url_for, flash, session, redirect
from app.forms import LoginForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    print('dasdsdsd')
    if login_form.validate_on_submit():
        print(login_form.validate_on_submit())
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usario registrado con éxito!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', **context)
