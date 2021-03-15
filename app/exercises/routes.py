from flask import request, current_app
from . import bp
from .exercise_request_handlers import (
    ExerciseCommandRequestHandler,
    ExerciseQueryRequestHandler,
)
from .exercise_response import ExerciseResponse
from .tag_handler import TagCommandHandler

# to remove
# from .exerciseDataManager import *


# @bp.route("/new", methods=["GET", "POST"])
# def exerciseNew():
#     return exerciseNewImpl()


@bp.route("/list", methods=["GET"])
def exerciseList():
    return exerciseListImpl()


@bp.route("/<name>", methods=["GET", "POST"])
def exerciseShowName(name):
    return exerciseShowNameImpl(name)


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def exerciseEdit(id):
    return exerciseEditImpl(id)


# Serialized
@bp.route("/list/serialized", methods=["GET"])
def exerciseListSerialized():
    return exerciseListSerializedImpl()


@bp.route("/<int:id>/serialized", methods=["GET"])
def exerciseIdSerialize(id):
    return exerciseIdSerializeImpl(id)


@bp.route("/create", methods=["POST"])
def exerciseCreateSerialized():
    return ExerciseCommandRequestHandler.exercise_create()


@bp.route("/<int:id>/update", methods=["POST"])
def exerciseCreateUpdate(id):
    return ExerciseCommandRequestHandler.exercise_update(id)


@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def exerciseDelete(id):
    return ExerciseCommandRequestHandler.exercise_delete(id)


@bp.route("/<name>/serialized", methods=["GET"])
def exerciseShowNameSerialized(name):
    return ExerciseQueryRequestHandler.find_by_name(name)


# tags
@bp.route("/tag/create", methods=["POST"])
def tag_create():
    return TagCommandHandler.tag_create()


@bp.route("/tag/<int:id>/update", methods=["POST"])
def tag_update(id):
    return TagCommandHandler.tag_update(id)


# @bp.route("/tags/list", methods=["GET"])
# def tagsListSerialized():
#     return tagsListSerializedImpl()
