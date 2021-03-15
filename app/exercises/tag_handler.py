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
from werkzeug.urls import url_parse

# from app.exercises.forms import ExerciseForm
from app.exercises.validators import TagValidator
from json import dumps
from .exercise_response import ExerciseResponse
from .models import TagCommand, Tag

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


class TagCommandHandler:
    @staticmethod
    def tag_create():
        tag_params = request.get_json()
        validation_result = TagValidator.validate(tag_params)
        if validation_result is False:
            return ExerciseResponse.error_not_json()
        if TagCommand.create_if_not_in_db(tag_params) is False:
            return ExerciseResponse.error_can_not_be_created_already_exist()
        else:
            return ExerciseResponse.ok_created()

    @staticmethod
    def tag_update(id):
        tag_params = request.get_json()
        validation_result = TagValidator.validate(tag_params)
        if validation_result is False:
            return ExerciseResponse.error_not_json()
        if not TagCommand.update(id, tag_params):
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_updated()

    @staticmethod
    def tag_delete(id):
        if not TagCommand.delete(id):
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_updated()
