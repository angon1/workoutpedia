from app.excercises.models import Excercise
from app.excercises.excercise_response import ExcerciseResponse
from app.excercises.validators import ExcerciseValidator
from flask import (
    request,
)


class ExcerciseRequestHandler:
    @staticmethod
    def create():
        excercise_params = ExcerciseValidator.validate_request_and_return_dictionary(
            request
        )
        if Excercise.create_or_none_if_already_in_db(excercise_params) is False:
            return ExcerciseResponse.error_can_not_be_created_already_exist()
        else:
            return ExcerciseResponse.ok_created()

    @staticmethod
    def update(id):
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
    def delete(id):
        if Excercise.remove_from_db(id) is False:
            return ExcerciseResponse.error_not_found()
        else:
            return ExcerciseResponse.ok_deleted()
