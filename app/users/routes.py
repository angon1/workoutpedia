from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import logout_user
from app.users.loginRoutines import *
from app.users.userHandling import *
from app.users import bp


#user pages
@bp.route('/user/<username>')
def user(username):
    return renderUserPage(username)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return loginWorker()


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return registerWorker()
