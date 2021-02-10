from flask import (
    request,
    make_response,
)


class ExerciseResponse:
    def __init__(self, code=200, msg=""):
        self.message_dict = {"message": msg}
        self.status_code = code

    def update(self, code, msg):
        self.message_dict = msg
        self.status_code = code

    def prepare(self):
        return make_response(self.message_dict, self.status_code)

    @classmethod
    def error_not_json(cls):
        return cls(400, "Request body must be proper tag JSON").prepare()

    @classmethod
    def error_not_found(cls):
        return cls(400, "Exercise not found").prepare()

    @classmethod
    def error_can_not_be_created_already_exist(cls):
        return cls(400, "Exercise can't be created, already in base").prepare()

    @classmethod
    def ok_created(cls):
        return cls(200, "Succesfuly added to base").prepare()

    @classmethod
    def ok_updated(cls):
        return cls(200, "Succesfuly updated exercise in base").prepare()

    @classmethod
    def ok_deleted(cls):
        return cls(200, "Exercise deleted").prepare()

    @classmethod
    def ok_exercise_found(cls, exercise):
        response = cls()
        response.update(200, exercise)
        return response.prepare()

    @classmethod
    def ok_tags_list_found(cls, tags_list):
        response = cls()
        response.update(200, tags_list)
        return response.prepare()
