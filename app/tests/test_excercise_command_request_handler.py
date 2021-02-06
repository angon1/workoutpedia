from flask import current_app, request
from flask import url_for, json, jsonify
from app.exercises.models import Exercise, Tag
from app.exercises.exercise_request_handlers import ExerciseCommandRequestHandler
from app.exercises.exercise_response import ExerciseResponse


class TestExerciseCommandRequestHandler:
    def test_processing_create_exercise_request_and_success(
        self, client, test_exercise
    ):
        with current_app.test_request_context(method="POST", json=test_exercise):
            response = ExerciseCommandRequestHandler.exercise_create()
        assert response.status_code == ExerciseResponse.ok_created().status_code
        assert client.get("exercises/unittest1/serialized").status_code == 200

    def test_processing_create_exercise_request_and_fail(
        self, client, test_exercise, new_exercise
    ):
        with current_app.test_request_context(method="POST", json=test_exercise):
            response = ExerciseCommandRequestHandler.exercise_create()
        assert (
            response.status_code
            == ExerciseResponse.error_can_not_be_created_already_exist().status_code
        )

    def test_delete_exercise_from_db_and_success(
        self, client, new_exercise, test_exercise
    ):
        with current_app.test_request_context(method="POST", json=test_exercise):
            response = ExerciseCommandRequestHandler.exercise_delete(new_exercise.id)
        assert response.status_code == ExerciseResponse.ok_deleted().status_code

    def test_delete_exercise_from_db_and_fail_because_not_exist(self, client):
        response = ExerciseCommandRequestHandler.exercise_delete(987)
        assert response.status_code == ExerciseResponse.error_not_found().status_code

    def test_update_exercise_and_fail_because_exercise_does_not_exist(
        self, client, test_exercise
    ):
        with current_app.test_request_context(method="POST", json=test_exercise):
            response = ExerciseCommandRequestHandler.exercise_update(987)
        assert response.status_code == ExerciseResponse.error_not_found().status_code

    def test_update_exercise_and_success(self, client, test_exercise, new_exercise):
        with current_app.test_request_context(method="POST", json=test_exercise):
            response = ExerciseCommandRequestHandler.exercise_update(new_exercise.id)
        assert response.status_code == ExerciseResponse.ok_updated().status_code
        assert client.get("exercises/unittest1/serialized").status_code == 200

    # Dispatcher.ExerciseHandler.costam.funkja()
    # DispatcherInterface()
    # DisptarchersUtilty() - elemnty wspolne

    # def - create, update, get, get_id, get_name, get_list - permisions for users

    # def test_add_tag_to_exercise_success()

    # def test_add_tag_to_exercise_fail_tag_alredy_added()

    # def test_get_tags_for_exercise()

    # def test_remove_tag_from_exercise_success()

    # def test_remove_tag_from_exercise_fail_no_tag()
