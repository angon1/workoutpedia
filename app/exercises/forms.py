from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.exercises.models import *


class ExerciseForm(FlaskForm):
    name = StringField("Exercise name", validators=[DataRequired()])
    description = StringField("Exercise Description", validators=[DataRequired()])
    movieLink = StringField("Link to YouTube")
    submit = SubmitField("Save")


class TagForm(FlaskForm):
    name = StringField("Exercise name", validators=[DataRequired()])
    category = StringField("Exercise Description", validators=[DataRequired()])
    movieLink = StringField("Link to YouTube")
    submit = SubmitField("Save")
