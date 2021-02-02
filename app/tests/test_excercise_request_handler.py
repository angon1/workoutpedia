from flask import current_app, request
from flask import url_for, json, jsonify
from app.exercises.models import Exercise, Tag
from app.exercises.exercise_request_manager import ExerciseRequestManager
from app.exercises.exercise_response import ExerciseResponse


class TestExerciseRequestManager:
    def test_processing_create_exercise_request_and_success(
        self, client, test_exercise
    ):
        with current_app.test_request_context(method="POST", json=test_exercise):
            print("\n\nrequest = {}".format(request))
            # ExerciseRequestHandler.process_create_request()
            response = ExerciseRequestManager.exercise_create()
            print("\n\n tralala: response: {}\n".format(response))
        print(response.status_code)

        assert response.status_code == ExerciseResponse.ok_created().status_code

    def test_processing_create_exercise_request_and_fail(
        self, client, test_exercise, new_exercise
    ):
        with current_app.test_request_context(method="POST", json=test_exercise):
            print("\n\nrequest = {}".format(request))
            # ExerciseRequestHandler.process_create_request()
            response = ExerciseRequestManager.exercise_create()
        assert (
            response.status_code
            == ExerciseResponse.error_can_not_be_created_already_exist().status_code
        )

    # Dispatcher.ExerciseHandler.costam.funkja()
    # DispatcherInterface()
    # DisptarchersUtilty() - elemnty wspolne

    # def - create, update, get, get_id, get_name, get_list - permisions for users

    # def test_delete_exercise_from_db_and_success()

    # def test_delete_exercise_from_db_and_fail()

    # def test_update_exercise_and_fail_because_exercise_does_not_exist()

    # def def test_processing_create_exercise_request_and_fail_because_exercise_exist()

    # def test_update_exercise_and_success()

    # def test_add_tag_to_exercise_success()

    # def test_add_tag_to_exercise_fail_tag_alredy_added()

    # def test_get_tags_for_exercise()

    # def test_remove_tag_from_exercise_success()

    # def test_remove_tag_from_exercise_fail_no_tag()
