from app import app
from app.excercises.models import *
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.users.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.users.models import *
