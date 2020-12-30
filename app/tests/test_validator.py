from flask import current_app
from flask import url_for, json, jsonify
from app.excercises.models import Excercise,Tag
from app.excercises.validators import ExcerciseValidator, TagValidator

class TestValidators:
    def test_validate_excercise_json(self, client, test_excercise):
        """
        GIVEN correct json of Excercise
        WHEN validator for excercise is called
        THEN check if True is returned
        """
        data = json.dumps(test_excercise)
        print(data)
        assert True == ExcerciseValidator.validate(data)

    def test_validate_excercise_incorrect_json(self, client, test_excercise_incorrect):
        """
        GIVEN incorrect json of Excercise
        WHEN validator for excercise is called
        THEN check if True is returned
        """
        data = json.dumps(test_excercise_incorrect)
        print(data)
        assert False == ExcerciseValidator.validate(data)

    def test_validate_tag_incorrect_json(self, client, test_tags_incorrect):
        """
        GIVEN incorrect json of Tag
        WHEN validator for Tag is called
        THEN check if True is returned
        """
        data = json.dumps(test_tags_incorrect)
        print(data)
        assert False == TagValidator.validate(data)

    def test_validate_tag_correct_json(self, client, test_tags):
        """
        GIVEN incorrect json of Tag
        WHEN validator for Tag is called
        THEN check if True is returned
        """
        data = json.dumps(test_tags)
        print(data)
        assert True == TagValidator.validate(data)
