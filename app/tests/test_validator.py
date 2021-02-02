from flask import current_app
from flask import url_for, json, jsonify
from app.exercises.models import Exercise, Tag
from app.exercises.validators import ExerciseValidator, TagValidator


class TestValidators:
    def test_validate_exercise_json(self, client, test_exercise):
        """
        GIVEN correct json of Exercise
        WHEN validator for exercise is called
        THEN check if True is returned
        """
        data = json.dumps(test_exercise)
        print(data)
        assert True == ExerciseValidator.validate(data)

    def test_validate_exercise_incorrect_json(self, client, test_exercise_incorrect):
        """
        GIVEN incorrect json of Exercise
        WHEN validator for exercise is called
        THEN check if True is returned
        """
        data = json.dumps(test_exercise_incorrect)
        print(data)
        assert False == ExerciseValidator.validate(data)

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
