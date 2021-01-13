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
from app.excercises.models import *
from werkzeug.urls import url_parse
from app.excercises.forms import ExcerciseForm
from json import dumps


class ExcerciseValidator:
    def validate(data):
        if "name" and "description" and "movieLink" in data:
            return True
        else:
            return False

    def validate_request(request):
        excercise_params = request.get_json()
        if "name" and "description" and "movieLink" in excercise_params:
            return excercise_params
        else:
            return False


class TagValidator:
    def validate(data):
        if "name" and "category" in data:
            return True
        else:
            return False
