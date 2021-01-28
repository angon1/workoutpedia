from flask import request, current_app
from . import bp
from .excercise_request_handler import ExcerciseRequestHandler
from .excercise_response import ExcerciseResponse

# to remove
from .excerciseDataHandler import *


# @bp.route("/new", methods=["GET", "POST"])
# def excerciseNew():
#     return excerciseNewImpl()


@bp.route("/list", methods=["GET"])
def excerciseList():
    return excerciseListImpl()


@bp.route("/<name>", methods=["GET", "POST"])
def excerciseShowName(name):
    return excerciseShowNameImpl(name)


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def excerciseEdit(id):
    return excerciseEditImpl(id)


# Serialized
@bp.route("/list/serialized", methods=["GET"])
def excerciseListSerialized():
    return excerciseListSerializedImpl()


@bp.route("/<int:id>/serialized", methods=["GET"])
def excerciseIdSerialize(id):
    return excerciseIdSerializeImpl(id)


@bp.route("/create", methods=["POST"])
def excerciseCreateSerialized():
    return ExcerciseRequestHandler.create()


@bp.route("/<int:id>/update", methods=["POST"])
def excerciseCreateUpdate(id):
    return ExcerciseRequestHandler.update(id)


@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def excerciseDelete(id):
    return ExcerciseRequestHandler.delete(id)


@bp.route("/<name>/serialized", methods=["GET"])
def excerciseShowNameSerialized(name):
    return ExcerciseRequestHandler.find_exercise_by_name(name)


# tags
# @bp.route("/tags/list", methods=["GET"])
# def tagsListSerialized():
#     return tagsListSerializedImpl()
