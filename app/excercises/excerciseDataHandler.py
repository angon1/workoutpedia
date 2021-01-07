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
            name=excercise_params["name"], description=excercise_params["description"], movieLink=excercise_params["movieLink"]
        )
        db.session.add(excercise)
        db.session.commit()
        return ExcerciseResponse(200, {"message": "Succesfuly added to base"})
    else:
        excercise.name = excercise_params["name"]
        excercise.description = excercise_params["description"]
        excercise.movieLink = excercise_params["movieLink"]
        db.session.commit()
        return ExcerciseResponse(200, {"message": "Succesfuly updated excercise in base"})


def get_excercise_or_none(name):
    return Excercise.query.filter_by(name=name).first()


def excercise_update(excercise_params):
    result = [{"": ""}, 200]
    excercise = get_excercise_or_none(excercise_params["name"])
    if excercise is None:
        result[0] = {"message": "Not found"}
        result[1] = 400
    else:
        excercise.name = excercise_params["name"]
        excercise.description = excercise_params["description"]
        excercise.movieLink = excercise_params["movieLink"]
        result[0] = {"message": "Succesfuly updated excercise in base"}
        result[1] = 200


    db.session.commit()
    return result

def excerciseRemoveFromBaseDict(excercise_params):
    excercise = get_excercise_or_none(excercise_params["name"])
    if excercise is None:
        return ExcerciseResponse(400, {"message": "Excercise not found in base"})
    else:
        db.session.delete(excercise)
        db.session.commit()
        return ExcerciseResponse(200, {"message": "Excercise deleted"})




def check_if_request_is_json():
    if request.is_json:
        return request.get_json()
    else:
        return False

def zmien_te_nazwe(request, action):
    if action == "create" or action == "update":
        return excerciseAddToBaseDict(request)
    elif action == "delete":
        return excerciseRemoveFromBaseDict(request)

class ExcerciseResponse:
    def __init__(self, code, msg):
        self.message_dict = msg
        self.status_code = code

    def update(self, code, msg):
        self.message_dict = msg
        self.status_code = code

    def prepare(self):
        return make_response(self.message_dict, self.status_code)



class ExcerciseRequestHandler:
    def __init__(self):
        self.response_message_field = 0
        self.response_code_field = 1
        self.response = ExcerciseResponse(200, {"":""})

    def handleIncomingJson(self, action):
        if request.is_json:
            excercise_params = request.get_json()
            if ExcerciseValidator.validate(excercise_params):
                self.response = zmien_te_nazwe(excercise_params, action)
            else:
                self.response.update(400, {"message": "Invalid excercise format"})
        else:
            self.response.update(400, {"message": "Request body must be JSON"})
        return self.response.prepare()

    @staticmethod
    def create():
        return ExcerciseRequestHandler().handleIncomingJson("create")

    @staticmethod
    def update(id):
        return ExcerciseRequestHandler().handleIncomingJson("update")

    @staticmethod
    def delete(id):
        return ExcerciseRequestHandler().handleIncomingJson("delete")
