from flask import request, current_app
from . import bp
from .excercise_request_manager import ExcerciseRequestManager
from .excercise_response import ExcerciseResponse

# to remove
# from .excerciseDataManager import *


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
    return ExcerciseRequestManager.exercise_create()


@bp.route("/<int:id>/update", methods=["POST"])
def excerciseCreateUpdate(id):
    return ExcerciseRequestManager.exercise_update(id)


@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def excerciseDelete(id):
    return ExcerciseRequestManager.exercise_delete(id)


@bp.route("/<name>/serialized", methods=["GET"])
def excerciseShowNameSerialized(name):
    return ExcerciseRequestManager.exercise_find_by_name(name)


# tags
# @bp.route("/tags/list", methods=["GET"])
# def tagsListSerialized():
#     return tagsListSerializedImpl()
