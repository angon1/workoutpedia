from flask import render_template, flash, redirect, url_for, request
from app import app
from flask_login import logout_user
from app.users.loginRoutines import *
from app.excercises.excerciseDataHandler import excerciseNewImpl

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
