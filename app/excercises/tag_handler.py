from flask import current_app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app.excercises.models import *
from werkzeug.urls import url_parse
from app.excercises.forms import ExcerciseForm
from app.excercises.validators import ExcerciseValidator
from json import dumps

#Tags - Excercise categorization
class TagHandler:
    def get_json_list(self):
        tags = Tag.query.all()
        serializedTagsList = []
        for tag in tags:
            serializedTagsList.append(tag.asDict())
        return jsonify(serializedTagsList)

    def get_json_by_id(self, id):
        tag = Tag.query.get(id)
        tagJson = tag.asDict()
        return jsonify(tagJson)

    def get_with_connected_excercises_json(self, id):
        tag = Tag.query.get(id)
        excercises = tag.getExcercises()
        tagWithExcercises = []
        tagWithExcercises.append(tag.asDict())
        tagWithExcercises.append(excercises)
        return jsonify(tagWithExcercises)

    def get_connected_excercies_json(self, id):
        tag = Tag.query.get(id)
        excercises = excercises = tag.getExcercises()
        return jsonify(excercises)

    def get_json_by_category(self, category):
        tags = Tag.query.filter_by(category=category)
        serializedTags = []
        for tag in tags:
            serializedTags.append(tag.asDict())
        return jsonify(serializedTags)
