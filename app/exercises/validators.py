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
    def validate(request):
        tag = request.get_json()
        print(tag)
        if (tag is not None) and ("name" and "category" in tag):
            return tag
        else:
            return False
