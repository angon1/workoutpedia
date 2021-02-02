from flask import current_app, request
from flask import url_for, json, jsonify
from app.excercises.models import Excercise, Tag
from app.excercises.excercise_request_manager import ExcerciseRequestManager


class TestExcerciseRequestManager:
    def test_processing_create_excercise_request_and_success(
        self, client, test_excercise
    ):
        with current_app.test_request_context(method="POST", json=test_excercise):
            print("\n\nrequest = {}".format(request))
            # ExcerciseRequestHandler.process_create_request()
            ExcerciseRequestManager.exercise_create()
        assert client.get("excercises/unittest1/serialized").status_code == 200

    def test_processing_create_excercise_request_and_fail(
        self, client, test_excercise, new_excercise
    ):
        with current_app.test_request_context(method="POST", json=test_excercise):
            print("\n\nrequest = {}".format(request))
            # ExcerciseRequestHandler.process_create_request()
            ExcerciseRequestManager.exercise_create()
        assert client.get("excercises/unittest1/serialized").status_code == 200

    # Dispatcher.ExcerciseHandler.costam.funkja()
    # DispatcherInterface()
    # DisptarchersUtilty() - elemnty wspolne

    # def - create, update, get, get_id, get_name, get_list - permisions for users

    # def test_delete_excercise_from_db_and_success()

    # def test_delete_excercise_from_db_and_fail()

    # def test_update_excercise_and_fail_because_exercise_does_not_exist()

    # def def test_processing_create_excercise_request_and_fail_because_exercise_exist()

    # def test_update_exercise_and_success()

    # def test_add_tag_to_excercise_success()

    # def test_add_tag_to_excercise_fail_tag_alredy_added()

    # def test_get_tags_for_exercise()

    # def test_remove_tag_from_exercise_success()

    # def test_remove_tag_from_exercise_fail_no_tag()
