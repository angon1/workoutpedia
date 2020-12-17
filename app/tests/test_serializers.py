from flask import current_app
from flask import url_for
from app.excercises.models import Excercise,Tag


def test_new_excercise(client, new_excercise, test_excercise):
    assert client.get("excercises/unittest1/serialized").status_code == 200
