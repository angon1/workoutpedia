from app.exercises.models import Exercise, ExerciseCommand, ExerciseQuery
from app.exercises.exercise_response import ExerciseResponse
from app.exercises.validators import ExerciseValidator
from flask import (
    request,
)
from flask import jsonify

# zmiana stanu bazy - create, delete, update,
class ExerciseCommandRequestHandler:
    @staticmethod
    def exercise_create():
        exercise_params = ExerciseValidator.validate_request_and_return_dictionary(
            request
        )
        if ExerciseCommand.create_or_none_if_already_in_db(exercise_params) is False:
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
        if not ExerciseCommand.update(id, exercise_params):
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_updated()

    @staticmethod
    def exercise_delete(id):
        if ExerciseCommand.remove_from_db(id) is False:
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_deleted()


# odpytanie - query - get, findy, etc - new/edit - jeśli występuje
class ExerciseQueryRequestHandler:
    @staticmethod
    def find_by_name(name):
        exercise = ExerciseQuery.get_name_from_db_or_none(name)
        if exercise is None:
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_exercise_found(exercise.asDict())

    @staticmethod
    def find_by_id(id):
        exercise = ExerciseQuery.get_from_db_or_none(id)
        if exercise is None:
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_exercise_found(exercise.asDict())

    @staticmethod
    def get_tags_list(id):
        tags_list = ExerciseQuery.get_tags_list_from_db_or_none(id)
        if tags_list is None:
            return ExerciseResponse.error_not_found()
        else:
            return ExerciseResponse.ok_tags_list_found(tags_list)
