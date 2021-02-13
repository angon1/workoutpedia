from flask import current_app, request
from flask import url_for, json, jsonify

from app.exercises.exercise_request_handlers import ExerciseQueryRequestHandler
from app.exercises.exercise_response import ExerciseResponse


class TestExerciseQueryRequestHandler:
    def test_get_exercise_from_db_by_id_and_success(self, client, new_exercise):
        response = ExerciseQueryRequestHandler.find_by_id(new_exercise.id)
        assert response.status_code == ExerciseResponse.ok_created().status_code
        assert client.get("exercises/unittest1/serialized").status_code == 200

    def test_get_exercise_from_db_by_id_and_fail(self, client):
        response = ExerciseQueryRequestHandler.find_by_id(987)
        assert response.status_code == ExerciseResponse.error_not_found().status_code

    def test_get_exercise_from_db_by_name_and_success(self, client, new_exercise):
        response = ExerciseQueryRequestHandler.find_by_name(new_exercise.name)
        assert response.status_code == ExerciseResponse.ok_created().status_code
        assert client.get("exercises/unittest1/serialized").status_code == 200

    def test_get_exercise_from_db_by_name_and_fail(self, client):
        response = ExerciseQueryRequestHandler.find_by_name("unittest1")
        assert response.status_code == ExerciseResponse.error_not_found().status_code

    def test_get_exercise_tag_list_and_success(self, client, new_exercise_with_tags):
        response = ExerciseQueryRequestHandler.get_tags_list(new_exercise_with_tags.id)
        assert (
            response.status_code == ExerciseResponse.ok_tags_list_found("").status_code
        )

    def test_get_exercise_tag_list_and_fail(self, client, test_exercise):
        response = ExerciseQueryRequestHandler.get_tags_list(987)
        assert response.status_code == ExerciseResponse.error_not_found().status_code
