# from app import app
# import unittest
from flask import current_app
from app.excercises.models import Excercise, Tag



#excercise tests
class TestExcercise:
    def test_new_excercise(self, app, new_excercise, test_excercise):
        """
        GIVEN a Excercise model
        WHEN a new Excercise is created
        THEN check the name, description and link values
        """
        assert new_excercise.name == test_excercise['name']
        assert new_excercise.description == test_excercise['description']
        assert new_excercise.movieLink == test_excercise['movieLink']

    def test_addTag(self, app, new_excercise, new_tags):
        """
        GIVEN a Excercise model object
        WHEN call Excercise.addTag with correct values
        THEN check if 'True' is returned
        """
        assert new_excercise.addTag(new_tags[0]) == True

    def test_removeTagTrue(self, app, new_excercise, new_tags):
        """
        GIVEN a Excercise model object
        WHEN call Excercise.removeTag with correct values
        THEN check if 'True' is returned
        """
        new_excercise.addTag(new_tags[0])
        assert new_excercise.removeTag(new_tags[0]) == True

    def test_removeTagFalse(self, app, new_excercise, new_tags):
        """
        GIVEN a Excercise model object
        WHEN call Excercise.removeTag with wrong values (Tag not in Excercise)
        THEN check if 'False' is returned
        """
        assert new_excercise.removeTag(new_tags[0]) == False

    def test_tagsDict(self, new_excercise, new_tags):
        """
        GIVEN a Excercise model object
        WHEN call Excercise.removeTag with wrong values (Tag not in Excercise)
        THEN check if 'False' is returned
        """
        new_excercise.addTag(new_tags[0])
        new_excercise.addTag(new_tags[1])

        assert (new_tags[0].asDict() == new_excercise.tagsDict()[0])
        assert (new_tags[1].asDict() == new_excercise.tagsDict()[1])

#tag tests
class TestTags:
    def test_new_tags(app, new_tags, test_tags):
        """
        GIVEN a Tag model
        WHEN  2 new Tags are created
        THEN check the name and category values
        """
        assert new_tags[0].name == test_tags[0]['name']
        assert new_tags[0].category == test_tags[0]['category']

        assert new_tags[1].name == test_tags[1]['name']
        assert new_tags[1].category == test_tags[1]['category']
