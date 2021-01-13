from flask import current_app
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    jsonify,
    make_response,
)
from app.excercises.models import *
from werkzeug.urls import url_parse
from app.excercises.forms import ExcerciseForm
from app.excercises.validators import ExcerciseValidator
from app.excercises.tag_handler import TagHandler
from json import dumps


def excerciseAddToBase(form):
    excercise = Excercise(
        name=form.name.data,
        description=form.description.data,
        movieLink=form.movieLink.data,
    )
    db.session.add(excercise)
    db.session.commit()
    flash("Excercise added to db")


def excerciseNewImpl():
    form = ExcerciseForm()
    if form.validate_on_submit():
        excerciseAddToBase(form)
        return redirect(url_for("main"))
    flash("Somehow Excercise can't be added")
    return render_template("edit.html", title="WorkoutPedia", form=form)


def excerciseEditOnSubmit(id, form):
    excercise = Excercise.query.get(id)
    excercise.name = form.name.data
    excercise.description = form.description.data
    excercise.movieLink = form.movieLink.data
    db.session.commit()
    excercise = Excercise.query.get(id)
    flash("Excercise changes saved")
    return render_template("show.html", title="WorkoutPedia", excercise=excercise)


def excerciseEditOnGet(id, form):
    excercise = Excercise.query.get(id)
    form.name.data = excercise.name
    form.description.data = excercise.description
    form.movieLink.data = excercise.movieLink
    return render_template("edit.html", title="WorkoutPedia", id=id, form=form)


def excerciseEditImpl(id):
    form = ExcerciseForm()
    if form.validate_on_submit():
        return excerciseEditOnSubmit(id, form)
    elif request.method == "GET":
        return excerciseEditOnGet(id, form)


def excerciseGetAllFromBase():
    return Excercise.query.all()


def excerciseListImpl():
    excerciseList = excerciseGetAllFromBase()
    return render_template(
        "index.html", title="WorkoutPedia", excerciseList=excerciseList
    )


def excerciseGetFromBase(name):
    return Excercise.query.filter_by(name=name).first()


def excerciseShowNameImpl(name):
    excercise = excerciseGetFromBase(name)
    return render_template("show.html", title="WorkoutPedia", excercise=excercise)


def excerciseDeleteFromBase(id):
    excercise = Excercise.query.get(id)
    db.session.delete(excercise)
    db.session.commit()
    flash("Excercise {} succesfully removed from db".format(excercise.name))


def excerciseDeleteImpl(id):
    excerciseDeleteFromBase(id)
    return redirect(url_for("excerciseList"))


# Serializers
# excercises:
def excerciseListSerializedImpl():
    excerciseList = Excercise.query.all()
    serializedExcerciseList = []
    for i in excerciseList:
        serializedExcerciseList.append(i.to_dict(only=("id", "name")))
    return jsonify(serializedExcerciseList)


def excerciseListSerializedFullImpl():
    excerciseList = Excercise.query.all()
    serializedExcerciseList = []
    for excercise in excerciseList:
        serializedExcerciseList.append(excercise.asDict())
    return jsonify(serializedExcerciseList)


def excerciseShowNameSerializedImpl(name):
    excercise = Excercise.query.filter_by(name=name).one()
    excerciseJson = excercise.asDict()
    return jsonify(excerciseJson)


def excerciseIdSerializeImpl(id):
    excercise = Excercise.query.get(id)
    excerciseJson = excercise.asDict()
    return jsonify(excerciseJson)


def excerciseIdGetTagsImpl(id):
    excercise = Excercise.query.get(id)
    return jsonify(excercise.tagsDict())


# tag-excercise
def addTagsListToExcercise(id, tagsList):
    return Excercise.query.get(id).addTagsList(tagsList)


# Handle remote excercises routines
class ExcerciseResponse:
    def __init__(self, code, msg):
        self.message_dict = {"message": msg}
        self.status_code = code

    def update(self, code, msg):
        self.message_dict = msg
        self.status_code = code

    def prepare(self):
        return make_response(self.message_dict, self.status_code)


class ExcerciseParams:
    def __init__(self, json):
        self.params = json


class ExcerciseRequestHandler:
    @staticmethod
    def create():
        excercise_params = request.get_json()
        excercise = Excercise.create_or_none_if_already_in_db(excercise_params)
        if excercise is None:
            return ExcerciseResponse(400, "Excercise already in base").prepare()
        else:
            db.session.add(excercise)
            db.session.commit()
            return ExcerciseResponse(200, "Succesfuly added to base").prepare()

    @staticmethod
    def update(id):
        excercise_params = ExcerciseValidator.validate_request(request)
        if excercise_params is False:
            return ExcerciseResponse(
                400, "Request body must be proper excercise JSON"
            ).prepare()
        if not Excercise.update(id, excercise_params):
            return ExcerciseResponse(400, "Excercise not found").prepare()
        else:
            return ExcerciseResponse(
                200, "Succesfuly updated excercise in base"
            ).prepare()

    @staticmethod
    def delete(id):
        excercise = Excercise.get_from_db_or_none(id)
        if excercise is None:
            return ExcerciseResponse(400, "Excercise not found in base").prepare()
        else:
            db.session.delete(excercise)
            db.session.commit()
            return ExcerciseResponse(200, "Excercise deleted").prepare()

    # def get_json_from_request_or_none()

    # def return_error_when_no_json()
    #     ret response
