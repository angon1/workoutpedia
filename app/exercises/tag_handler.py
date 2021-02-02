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
from app.exercises.models import *
from werkzeug.urls import url_parse
from app.exercises.forms import ExerciseForm
from app.exercises.validators import ExerciseValidator
from json import dumps

# Tags - Exercise categorization
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

    def get_with_connected_exercises_json(self, id):
        tag = Tag.query.get(id)
        exercises = tag.getExercises()
        tagWithExercises = []
        tagWithExercises.append(tag.asDict())
        tagWithExercises.append(exercises)
        return jsonify(tagWithExercises)

    def get_connected_excercies_json(self, id):
        tag = Tag.query.get(id)
        exercises = exercises = tag.getExercises()
        return jsonify(exercises)

    def get_json_by_category(self, category):
        tags = Tag.query.filter_by(category=category)
        serializedTags = []
        for tag in tags:
            serializedTags.append(tag.asDict())
        return jsonify(serializedTags)
