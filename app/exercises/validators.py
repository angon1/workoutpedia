from flask import request


class ExerciseValidator:
    @staticmethod
    def validate(data):
        if "name" and "description" and "movieLink" in data:
            return True
        else:
            return False

    @staticmethod
    def validate_request_and_return_dictionary(request):
        exercise_params = request.get_json()
        if "name" and "description" and "movieLink" in exercise_params:
            return exercise_params
        else:
            return False


class TagValidator:
    @staticmethod
    def validate(tag_params):
        if tag_params is None:
            return False
        if "name" and "category" in tag_params:
            return True
        else:
            return False

    # @staticmethod
    # def validate_update_params():
