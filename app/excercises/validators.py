from flask import request


class ExcerciseValidator:
    @staticmethod
    def validate(data):
        if "name" and "description" and "movieLink" in data:
            return True
        else:
            return False

    @staticmethod
    def validate_request_and_return_dictionary(request):
        excercise_params = request.get_json()
        if "name" and "description" and "movieLink" in excercise_params:
            return excercise_params
        else:
            return False


class TagValidator:
    @staticmethod
    def validate(data):
        if "name" and "category" in data:
            return True
        else:
            return False
