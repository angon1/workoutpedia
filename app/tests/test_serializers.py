from flask import current_app
from flask.testing import FlaskClient
from flask import url_for


# def test_excercise_getById(app):
#     """
#     GIVEN a Excercise model
#     WHEN a new Excercise is created
#     THEN check the name, description and link values
#     """
#     assert FlaskClient.get("excercise").status_code == 200
#     # assert FlaskClient.get("excercise/3/serialized").status_code == 200




def test_new_excercise(new_excercise, test_excercise):
  app.test_client_class = FlaskClient
#   print("/exercise/{}/serialized".format(new_excercise.name))
#   url=url_for("/exercise/{}/serialized".format(new_excercise.name))
#   url = url_for('excerciseShowNameSerialized', name=new_excercise.name)
#   print("Testowy url {}".format(url))
  assert app.test_client().get("exercise/unittest1/serialized").status_code == 200
