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
    return render_template("excercises/edit.html", title='WorkoutPedia', form=form)

def excerciseEditOnSubmit(id,form):
    excercise = Excercise.query.get(id)
    excercise.name = form.name.data
    excercise.description = form.description.data
    excercise.movieLink = form.movieLink.data
    db.session.commit()
    excercise = Excercise.query.get(id)
    flash("Excercise changes saved")
    return render_template("excercises/show.html", title='WorkoutPedia', excercise=excercise)


def excerciseEditOnGet(id,form):
    excercise = Excercise.query.get(id)
    form.name.data = excercise.name
    form.description.data = excercise.description
    form.movieLink.data = excercise.movieLink
    return render_template("excercises/edit.html", title='WorkoutPedia', id=id, form=form)


def excerciseEditImpl(id):
    form = ExcerciseForm()
    if form.validate_on_submit():
        return excerciseEditOnSubmit(id,form)
    elif request.method == 'GET':
        return excerciseEditOnGet(id,form)





    # form = ExcerciseForm()
    # if form.validate_on_submit():
    #     current_user.username = form.username.data
    #     current_user.about_me = form.about_me.data
    #     db.session.commit()
    #     flash('Your changes have been saved.')
    #     return redirect(url_for('edit_profile'))
    # elif request.method == 'GET':
    #     form.name.data = current_user.username
    #     form.about_me.data = current_user.about_me
    # return render_template('edit_profile.html', title='Edit Profile',
    #                        form=form)


def excerciseGetAllFromBase():
    return Excercise.query.all()

def excerciseListImpl():
    excerciseList = excerciseGetAllFromBase()
    return render_template("excercises/index.html", title='WorkoutPedia', excerciseList=excerciseList)


def excerciseGetFromBase(name):
    return Excercise.query.filter_by(name=name).first()

def excerciseShowNameImpl(name):
    excercise = excerciseGetFromBase(name)
    return render_template("excercises/show.html", title='WorkoutPedia', excercise=excercise)

def excerciseDeleteFromBase(id):
    excercise = Excercise.query.get(id)
    db.session.delete(excercise)
    db.session.commit()
    flash('Excercise {} succesfully removed from db'.format(excercise.name))

def excerciseDeleteImpl(id):
    excerciseDeleteFromBase(id)
    return redirect(url_for('excerciseList'))
