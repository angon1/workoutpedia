from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app
from .users.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from .users.models import *

@app.route('/')
# @app.route('/users/')


@app.route('/main')
def main():
    excercises = [
        {
            'excercise': {'name': 'Push Up'},
            'description': 'Simple push up',
            'link': 'example_link'
        },
        {
            'excercise': {'name': 'Pull Up'},
            'description': 'Simple pull up',
            'link': 'example_link 2'
        }
    ]
    return render_template('main.html', title='WorkoutPedia', excercises=excercises)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))
