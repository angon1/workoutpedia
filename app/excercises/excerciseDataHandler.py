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
def excerciseAddToBaseDict(excercise_params):
    excercise = get_excercise_or_none(excercise_params["name"])
    if excercise is None:
        excercise = Excercise(
            name=excercise_params["name"],
            description=excercise_params["description"],
            movieLink=excercise_params["movieLink"],
        )
        db.session.add(excercise)
        db.session.commit()
        return ExcerciseResponse(200, "Succesfuly added to base")
    else:
        excercise.name = excercise_params["name"]
        excercise.description = excercise_params["description"]
        excercise.movieLink = excercise_params["movieLink"]
        db.session.commit()
        return ExcerciseResponse(200, "Succesfuly updated excercise in base")


def excerciseRemoveFromBaseDict(excercise_params):
    excercise = get_excercise_or_none(excercise_params["name"])
    if excercise is None:
        return ExcerciseResponse(400, "Excercise not found in base")
    else:
        db.session.delete(excercise)
        db.session.commit()
        return ExcerciseResponse(200, "Excercise deleted")


def check_if_request_is_json():
    if request.is_json:
        return request.get_json()
    else:
        return False


def zmien_te_nazwe(excercise_params, action):
    if action == "create":
        return excerciseAddToBaseDict(excercise_params)
    elif action == "update":
        return excerciseAddToBaseDict(excercise_params)
    elif action == "delete":
        return excerciseRemoveFromBaseDict(excercise_params)


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


def get_excercise_or_none(name):
    return Excercise.query.filter_by(name=name).first()


class ExcerciseRequestHandler:
    def __init__(self):
        self.excercise_params = request.get_json()
        self.response = ExcerciseResponse(200, "")

    def handle_request(self, action):
        if self.excercise_params is not None:
            self.response = zmien_te_nazwe(self.excercise_params, action)
        else:
            self.response.update(400, {"message": "Request body must be JSON"})
        return self.response.prepare()

    def update_proceed(self, excercise_params):
        excercise = Excercise.get_from_db_or_none(excercise_params["name"])
        if excercise is None:
            return ExcerciseResponse(400, "Excercise not found").prepare()
        else:
            excercise.name = excercise_params["name"]
            excercise.description = excercise_params["description"]
            excercise.movieLink = excercise_params["movieLink"]
            db.session.commit()
            return ExcerciseResponse(
                200, "Succesfuly updated excercise in base"
            ).prepare()

    @staticmethod
    def create():
        return ExcerciseRequestHandler().handle_request("create")

    @staticmethod
    def update(id):
        excercise_params = request.get_json()
        if excercise_params is None:
            return ExcerciseResponse(
                400, {"message": "Request body must be JSON"}
            ).prepare()
        if ExcerciseValidator.validate(excercise_params):
            return ExcerciseRequestHandler().update_proceed(excercise_params)
        else:
            return ExcerciseResponse(
                400, {"message": "Excercise params from request not valid"}
            ).prepare()

    @staticmethod
    def delete(id):
        return ExcerciseRequestHandler().handle_request("delete")

    # def get_json_from_request_or_none()

    # def return_error_when_no_json()
    #     ret response
