# from app import app
# import unittest
from flask import current_app
from app.exercises.models import Exercise, Tag


# exercise tests
class TestExercise:
    def test_new_exercise(self, app, new_exercise, test_exercise):
        """
        GIVEN a Exercise model
        WHEN a new Exercise is created
        THEN check the name, description and link values
        """
        assert new_exercise.name == test_exercise["name"]
        assert new_exercise.description == test_exercise["description"]
        assert new_exercise.movieLink == test_exercise["movieLink"]

    def test_addTag(self, app, new_exercise, new_tags):
        """
        GIVEN a Exercise model object
        WHEN call Exercise.addTag with correct values
        THEN check if 'True' is returned
        """
        assert new_exercise.addTag(new_tags[0]) == True

    def test_removeTagTrue(self, app, new_exercise, new_tags):
        """
        GIVEN a Exercise model object
        WHEN call Exercise.removeTag with correct values
        THEN check if 'True' is returned
        """
        new_exercise.addTag(new_tags[0])
        assert new_exercise.removeTag(new_tags[0]) == True

    def test_removeTagFalse(self, app, new_exercise, new_tags):
        """
        GIVEN a Exercise model object
        WHEN call Exercise.removeTag with wrong values (Tag not in Exercise)
        THEN check if 'False' is returned
        """
        assert new_exercise.removeTag(new_tags[0]) == False

    def test_tagsDict(self, new_exercise, new_tags):
        """
        GIVEN a Exercise model object
        WHEN call Exercise.removeTag with wrong values (Tag not in Exercise)
        THEN check if 'False' is returned
        """
        new_exercise.addTag(new_tags[0])
        new_exercise.addTag(new_tags[1])

        assert new_tags[0].asDict() == new_exercise.tagsDict()[0]
        assert new_tags[1].asDict() == new_exercise.tagsDict()[1]


# tag tests
class TestTags:
    def test_new_tags(app, new_tags, test_tags):
        """
        GIVEN a Tag model
        WHEN  2 new Tags are created
        THEN check the name and category values
        """
        assert new_tags[0].name == test_tags[0]["name"]
        assert new_tags[0].category == test_tags[0]["category"]

        assert new_tags[1].name == test_tags[1]["name"]
        assert new_tags[1].category == test_tags[1]["category"]
