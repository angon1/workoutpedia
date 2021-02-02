# from flask import current_app, request
# from flask import url_for, json, jsonify
# from app.tags.models import Excercise, Tag
# from app.tags.tag_request_handler import ExcerciseRequestHandler


# class TestExcerciseRequestDispatcher:
#     def test_processing_create_tag_request_and_success(self, client, test_tag):
#         with current_app.test_request_context(method="POST", json=test_tag):
#             print("\n\nrequest = {}".format(request))
#             # ExcerciseRequestHandler.process_create_request()
#             ExerciseRequestDispatcher.process_create(request)
#         assert client.get("tags/unittest1/serialized").status_code == 200

#     # Dispatcher.ExcerciseHandler.costam.funkja()
#     # DispatcherInterface()
#     # DisptarchersUtilty() - elemnty wspolne

#     # def - create, update, get, get_id, get_name, get_list - permisions for users

#     # def test_delete_tag_from_db_and_success()

#     # def test_delete_tag_from_db_and_fail_no_tag()

#     # def test_update_tag_and_fail_because_tag_does_not_exist()

#     # def def test_processing_create_tag_request_and_fail_because_tag_exist()

#     # def test_update_tag_and_success()

#     # def test_get_exercises_with_tag_and_success()

#     # def test_get_exercises_with_tag_and_fail()

#     # def create_category_and_success()

#     # def create_category_and_fail_already_exist()
