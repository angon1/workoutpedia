from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask import current_app
from app.users.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.users.models import *

def renderUserPage(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/user.html', user=user)
