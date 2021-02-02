from app.excercises.models import Excercise
from app.excercises.excercise_response import ExcerciseResponse
from app.excercises.validators import ExcerciseValidator
from flask import (
    request,
)
from flask import jsonify


class ExcerciseRequestManager:
    @staticmethod
    def exercise_create():
        excercise_params = ExcerciseValidator.validate_request_and_return_dictionary(
            request
        )
        if Excercise.create_or_none_if_already_in_db(excercise_params) is False:
            return ExcerciseResponse.error_can_not_be_created_already_exist()
        else:
            return ExcerciseResponse.ok_created()

    @staticmethod
    def exercise_update(id):
        excercise_params = ExcerciseValidator.validate_request_and_return_dictionary(
            request
        )
        if excercise_params is False:
            return ExcerciseResponse.error_not_json()
        if not Excercise.update(id, excercise_params):
            return ExcerciseResponse.error_not_found()
        else:
            return ExcerciseResponse.ok_updated()

    @staticmethod
    def exercise_delete(id):
        if Excercise.remove_from_db(id) is False:
            return ExcerciseResponse.error_not_found()
        else:
            return ExcerciseResponse.ok_deleted()

    @staticmethod
    def exercise_find_by_name(name):
        excercise = Excercise.query.filter_by(name=name).one()
        excerciseJson = excercise.asDict()
        return ExcerciseResponse.ok_exercise_found(excerciseJson)

    @staticmethod
    def exercise_get_by_id(name):
        excercise = Excercise.query.filter_by(name=name).one()
        excerciseJson = excercise.asDict()
        return ExcerciseResponse.ok_exercise_found(excerciseJson)
