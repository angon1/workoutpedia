# from app import app
# import unittest
from app.excercises.models import Excercise, Tag

# class ExcerciseModelCase(unittest.TestCase):
#     def setUp(self):
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

def test_new_excercise(new_excercise):
    """
    GIVEN a Excercise model
    WHEN a new Excercise is created
    THEN check the name, description and link values
    """
    assert new_excercise.name == 'unittest1'
    assert new_excercise.description == 'description1'
    assert new_excercise.movieLink == 'link1'
