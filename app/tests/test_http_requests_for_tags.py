# from flask import current_app
# from flask import url_for, json, jsonify
# from app.exercises.models import Exercise, Tag


# class TestSerializers:
#     def test_serialized_exercise_get(self, client, new_exercise):
#         assert client.get("exercises/unittest1/serialized").status_code == 200

#     def test_exercise_dict(self, client, new_exercise):
#         """
#         GIVEN a Exercise model and exercise dictionary
#         WHEN GET is send to exercise url
#         THEN check if proper exercise dictionary is returned
#         """
#         exerciseDict = new_exercise.asDict()
#         data = json.loads(client.get("exercises/unittest1/serialized").get_data())
#         print(data)
#         assert data == exerciseDict

#     def test_exercise_add_post(self, client, test_exercise):
#         """
#         GIVEN a test exercise data
#         WHEN post  JSONified exercise data to exercise_add url
#         THEN check if exercise is added to db
#         """
#         exerciseJson = json.dumps(test_exercise)
#         print(exerciseJson)
#         response = client.post(
#             "exercises/create",
#             data=exerciseJson,
#             content_type="application/json",
#         )
#         data = json.loads(response.get_data(as_text=True))
#         print(data)
#         assert response.status_code == 200
#         assert data["message"] == "Succesfuly added to base"

#     def test_exercise_update_post(self, client, new_exercise, test_exercise):
#         """
#         GIVEN a test exercise data
#         WHEN post  JSONified exercise data to exercise_add url
#         THEN check if exercise is added to db
#         """
#         updateUrl = "exercises/{}/update".format(new_exercise.id)
#         exerciseJson = json.dumps(test_exercise)
#         print(updateUrl)
#         response = client.post(
#             updateUrl,
#             data=exerciseJson,
#             content_type="application/json",
#         )
#         data = json.loads(response.get_data(as_text=True))
#         print(data)
#         assert response.status_code == 200
#         assert data["message"] == "Succesfuly updated exercise in base"

#     def test_exercise_delete_post(self, client, new_exercise, test_exercise):
#         """
#         GIVEN a test exercise data
#         WHEN post  JSONified exercise data to exercise_add url
#         THEN check if exercise is added to db
#         """
#         deleteUrl = "exercises/{}/delete".format(new_exercise.id)
#         exerciseJson = json.dumps(test_exercise)
#         print(deleteUrl)
#         response = client.post(
#             deleteUrl,
#             data=exerciseJson,
#             content_type="application/json",
#         )
#         data = json.loads(response.get_data(as_text=True))
#         print(data)
#         assert response.status_code == 200
#         assert data["message"] == "Exercise deleted"

#     def test_exercise_delete_not_in_base_post(self, client, test_exercise):
#         """
#         GIVEN a test exercise data
#         WHEN post  JSONified exercise data to exercise_add url
#         THEN check if exercise is added to db
#         """
#         deleteUrl = "exercises/123/delete"
#         exerciseJson = json.dumps(test_exercise)
#         print(deleteUrl)
#         response = client.post(
#             deleteUrl,
#             data=exerciseJson,
#             content_type="application/json",
#         )
#         data = json.loads(response.get_data(as_text=True))
#         print(data)
#         assert response.status_code == 400
#         assert data["message"] == "Exercise not found"

#     # def test_tags_dict(self, client, new_tags):
#     #     """
#     #     GIVEN a Exercise model and exercise dictionary
#     #     WHEN GET is send to exercise url
#     #     THEN check if proper exercise dictionary is returned
#     #     """
#     #     tagsDict = []
#     #     data = json.loads(client.get("tags/serialized").get_data())
#     #     print(data)
#     #     assert data == tagsDict
