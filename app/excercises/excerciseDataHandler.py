from flask import current_app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app.excercises.models import *
from werkzeug.urls import url_parse
from app.excercises.forms import ExcerciseForm
from json import dumps


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


# Serializers
def serializeExcerciseList():
    excerciseList = Excercise.query.all()
    serializedExcerciseList = []
    for i in excerciseList:
        serializedExcerciseList.append(i.to_dict(only=('id', 'name')))
    return jsonify(serializedExcerciseList)

def serializeFullExcerciseList():
    excerciseList = Excercise.query.all()
    serializedExcerciseList = []
    for i in excerciseList:
        serializedExcerciseList.append(i.to_dict())
    return jsonify(serializedExcerciseList)


def excerciseListSerializedImpl():
    return serializeExcerciseList()

def excerciseListSerializedFullImpl():
    return serializeFullExcerciseList()

def serializeExcercise(name):
    excercise = Excercise.query.filter_by(name=name).one()
    excerciseJson = excercise.asDict()
    return jsonify(excerciseJson)

def excerciseShowNameSerializedImpl(name):
    return serializeExcercise(name)

def serializeExcerciseId(id):
    excercise = Excercise.query.get(id)
    excerciseJson = excercise.asDict()
    return jsonify(excerciseJson)

def excerciseIdSerializeImpl(id):
    return serializeExcerciseId(id)


def excerciseAddToBaseDict(req):
    excercise = Excercise.query.filter_by(name=req['name']).first()
    res = {"":""}
    if excercise is None:
        excercise = Excercise(name=req['name'], description=req['description'], movieLink=req['movieLink'])
        db.session.add(excercise)
        res = {"message": "Succesfuly added to base"}
    else:
        excercise.name = req['name']
        excercise.description = req['description']
        excercise.movieLink = req['movieLink']
        res = {"message": "Succesfuly updated excercise in base"}
    db.session.commit()
    return res

def validateIncomingExcerciseDict(req):
    if  'name' and 'description' and 'movieLink' in req:
        return True
    else:
        return False


def handleIncomingJson():
    res = {"":""}
    if request.is_json:
        req = request.get_json()
        if validateIncomingExcerciseDict(req):
            res = excerciseAddToBaseDict(req)
        else:
            res = {"message": "Invalid excercise format"}
    else:
        res = {"message": "Request body must be JSON"}
    return res

def excerciseCreateSerializedImpl():
    res = handleIncomingJson()
    return make_response(jsonify(res), 200)


#Excercise categorization
def addDisciplineToExcerciseByName(disciplineName, excerciseName):
    excercise = Excercise.query.filter_by(name=excerciseName).first()
    excercise.discipline.append(Discipline.query.filter_by(name=disciplineName).first())
    return True
