from flask import render_template, flash, redirect, url_for, request
from app import app
from flask_login import logout_user
from app.users.loginRoutines import *
from app.excercises.excerciseDataHandler import excerciseNewImpl, excerciseListImpl, excerciseShowNameImpl, excerciseDeleteImpl, excerciseEditImpl

@app.route('/')


@app.route('/main')
def main():
    return render_template('main.html', title='WorkoutPedia')


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

@app.route('/excercise/new', methods=['GET', 'POST'])
def excerciseNew():
    return excerciseNewImpl()

@app.route('/excercise/list', methods=['GET'])
def excerciseList():
    return excerciseListImpl()

@app.route('/excercise/<name>', methods=['GET', 'POST'])
def excerciseShowName(name):
    return excerciseShowNameImpl(name)

@app.route('/excercise/<int:id>/delete', methods=['GET', 'POST'])
def excerciseDelete(id):
    return excerciseDeleteImpl(id)

@app.route('/excercise/<int:id>/edit', methods=['GET', 'POST'])
def excerciseEdit(id):
    return excerciseEditImpl(id)

# @app.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     ]
#     return render_template('user.html', user=user)
