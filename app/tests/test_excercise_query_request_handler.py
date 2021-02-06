from flask import current_app, request
from flask import url_for, json, jsonify

# from app.exercises.models import Exercise, Tag
from app.exercises.exercise_request_handlers import ExerciseQueryRequestHandler
from app.exercises.exercise_response import ExerciseResponse


class TestExerciseQueryRequestHandler:
    def test_get_exercise_from_db_by_id_and_success(self, client, new_exercise):
        response = ExerciseQueryRequestHandler.find_by_id(new_exercise.id)
        assert response.status_code == ExerciseResponse.ok_created().status_code
        assert client.get("exercises/unittest1/serialized").status_code == 200

    def test_processing_create_exercise_request_and_fail(self, client):
        response = ExerciseQueryRequestHandler.find_by_id(987)
        assert response.status_code == ExerciseResponse.error_not_found().status_code

    # Dispatcher.ExerciseHandler.costam.funkja()
    # DispatcherInterface()
    # DisptarchersUtilty() - elemnty wspolne

    # def - create, update, get, get_id, get_name, get_list - permisions for users

    # def test_add_tag_to_exercise_success()

    # def test_add_tag_to_exercise_fail_tag_alredy_added()

    # def test_get_tags_for_exercise()

    # def test_remove_tag_from_exercise_success()

    # def test_remove_tag_from_exercise_fail_no_tag()
