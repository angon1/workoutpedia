from flask import render_template, flash, redirect, url_for, request, current_app
from app.excercises import bp
from app.excercises.excerciseDataHandler import *


@bp.route("/new", methods=["GET", "POST"])
def excerciseNew():
    return excerciseNewImpl()


@bp.route("/list", methods=["GET"])
def excerciseList():
    return excerciseListImpl()


@bp.route("/<name>", methods=["GET", "POST"])
def excerciseShowName(name):
    return excerciseShowNameImpl(name)


@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def excerciseDelete(id):
    return excerciseDeleteImpl(id)


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def excerciseEdit(id):
    return excerciseEditImpl(id)


# Serialized
@bp.route("/list/serialized", methods=["GET"])
def excerciseListSerialized():
    return excerciseListSerializedImpl()


@bp.route("/<name>/serialized", methods=["GET"])
def excerciseShowNameSerialized(name):
    return excerciseShowNameSerializedImpl(name)


@bp.route("/<int:id>/serialized", methods=["GET"])
def excerciseIdSerialize(id):
    return excerciseIdSerializeImpl(id)


@bp.route("/create", methods=["POST"])
def excerciseCreateSerialized():
    return ExcerciseRequestHandler.create()


@bp.route("/<int:id>/update", methods=["POST"])
def excerciseCreateUpdate(id):
    return ExcerciseRequestHandler.update(id)


@bp.route("/<int:id>/serialized/delete", methods=["POST"])
def excerciseDeleteSerialized(id):
    return ExcerciseRequestHandler.delete(id)


# tags
@bp.route("/tags/list", methods=["GET"])
def tagsListSerialized():
    return tagsListSerializedImpl()
