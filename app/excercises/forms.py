from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.excercises.models import *



class ExcerciseForm(FlaskForm):
    name = StringField('Excercise name', validators=[DataRequired()])
    description = StringField('Excercise Description', validators=[DataRequired()])
    movieLink = StringField('Link to YouTube')
    submit = SubmitField('Zapisz')
