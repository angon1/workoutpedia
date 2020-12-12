from flask import render_template, flash, redirect, url_for, request, current_app
# from app import app
from flask_login import logout_user
from app.users.loginRoutines import *
from app.users.userHandling import *
from app.excercises.excerciseDataHandler import excerciseNewImpl, excerciseListImpl, excerciseShowNameImpl, excerciseDeleteImpl, excerciseEditImpl, excerciseListSerializedImpl, excerciseShowNameSerializedImpl, excerciseIdSerializeImpl, excerciseCreateSerializedImpl

@app.route('/')


@app.route('/main')
def main():
    return render_template('main.html', title='WorkoutPedia')


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

#Serialized
@app.route('/excercise/list/serialized', methods=['GET'])
def excerciseListSerialized():
    return excerciseListSerializedImpl()

@app.route('/excercise/<name>/serialized', methods=['GET'])
def excerciseShowNameSerialized(name):
    return excerciseShowNameSerializedImpl(name)

@app.route('/excercise/<int:id>/serialized', methods=['GET'])
def excerciseIdSerialize(id):
    return excerciseIdSerializeImpl(id)

@app.route('/excercise/create', methods=['POST'])
def excerciseCreateSerialized():
    return excerciseCreateSerializedImpl()



#user pages
@app.route('/user/<username>')
def user(username):
    return renderUserPage(username)


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
