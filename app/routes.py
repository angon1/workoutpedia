from flask import render_template, flash, redirect, url_for
from app import app
from .users.forms import LoginForm

@app.route('/')
# @app.route('/users/')


@app.route('/main')
def main():
    user = {'username': 'Kuba'}
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
    return render_template('main.html', title='WorkoutPedia', user=user, excercises=excercises)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('main'))
    return render_template('login.html', title='Sign In', form=form)
