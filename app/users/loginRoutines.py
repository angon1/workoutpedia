from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask import current_app
from app.users.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.users.models import *


def loginValidateAndLogUser(form):
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
        flash("Invalid username or password")
        return redirect(url_for("login"))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get("next")
    if not next_page or url_parse(next_page).netloc != "":
        next_page = url_for("main")
    return next_page


def loginWorker():
    if current_user.is_authenticated:
        return redirect(url_for("main"))
    form = LoginForm()
    if form.validate_on_submit():
        next_page = loginValidateAndLogUser(form)
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


def registrationAddToDb(form):
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("Congratulations, you are now a registered user!")


def registerWorker():
    if current_user.is_authenticated:
        return redirect(url_for("main"))
    form = RegistrationForm()
    if form.validate_on_submit():
        registrationAddToDb(form)
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)
