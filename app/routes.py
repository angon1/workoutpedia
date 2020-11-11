from flask import render_template, flash, redirect, url_for, request
# from werkzeug.urls import url_parse
from app import app
# from .users.forms import LoginForm, RegistrationForm
from flask_login import logout_user
# from app.users.models import *
from app.users.loginRoutines import *

@app.route('/')


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
    return loginWorker()


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    return registerWorker()
