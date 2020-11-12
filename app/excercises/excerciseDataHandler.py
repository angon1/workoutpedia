from app import app
from app.excercises.models import *
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.excercises.forms import ExcerciseForm


def excerciseAddToBase(form):
    excercise = Excercise(name=form.name.data, description=form.description.data, movieLink=form.movieLink.data)
    db.session.add(excercise)
    db.session.commit()
    flash('Excercise added to db')


def excerciseNewImpl():
    form = ExcerciseForm()
    if form.validate_on_submit():
        excerciseAddToBase(form)
        return redirect(url_for('main'))
    flash('Somehow Excercise can\'t be added')
    return render_template("excerciseNew.html", title='WorkoutPedia', form=form)
