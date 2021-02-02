from app.exercises.models import Exercise
from app.exercises.exercise_response import ExerciseResponse
from app.exercises.validators import ExerciseValidator
from flask import (
    request,
)
from flask import jsonify


class ExerciseRequestManager:
    @staticmethod
    def exercise_create():
        exercise_params = ExerciseValidator.validate_request_and_return_dictionary(
            request
        )
        if Exercise.create_or_none_if_already_in_db(exercise_params) is False:
            return ExerciseResponse.error_can_not_be_created_already_exist()
        else:
            return ExerciseResponse.ok_created()

    @staticmethod
    def exercise_update(id):
        exercise_params = ExerciseValidator.validate_request_and_return_dictionary(
            request
        )
        if exercise_params is False:
            return ExerciseResponse.error_not_json()
        if not Exercise.update(id, exercise_params):
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_updated()

    @staticmethod
    def exercise_delete(id):
        if Exercise.remove_from_db(id) is False:
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_deleted()

    @staticmethod
    def exercise_find_by_name(name):
        exercise = Exercise.query.filter_by(name=name).one()
        exerciseJson = exercise.asDict()
        return ExerciseResponse.ok_exercise_found(exerciseJson)

    @staticmethod
    def exercise_get_by_id(name):
        exercise = Exercise.query.filter_by(name=name).one()
        exerciseJson = exercise.asDict()
        return ExerciseResponse.ok_exercise_found(exerciseJson)
