from flask import current_app, request
from flask import url_for, json, jsonify
from app.exercises.exercise_response import ExerciseResponse
from .conftest import TagDatabaseChecker
from app.exercises.tag_handler import TagCommandHandler


class TestTagCommandRequestHandler:
    def test_processing_create_tag_request_and_succeed(self, client, test_tag):
        with current_app.test_request_context(method="POST", json=test_tag):
            response = TagCommandHandler.tag_create()
        assert response.status_code == ExerciseResponse.ok_created().status_code
        assert TagDatabaseChecker.check_if_name_exist(test_tag["name"], client)

    def test_processing_create_tag_request_and_fail(self, client, test_tag, new_tags):
        with current_app.test_request_context(method="POST", json=test_tag):
            response = TagCommandHandler.tag_create()
        assert (
            response.status_code
            == ExerciseResponse.error_can_not_be_created_already_exist().status_code
        )
        assert TagDatabaseChecker.check_if_name_exist(test_tag["name"], client)

    def test_update_tag_and_fail_because_tag_does_not_exist(self, client, test_tag):
        with current_app.test_request_context(method="POST", json=test_tag):
            response = TagCommandHandler.tag_update("some_random_number")
            print(
                "response.status code: {}, respnse.message: {}".format(
                    response.status_code, response.data
                )
            )
        assert response.status_code == ExerciseResponse.error_not_found().status_code

    def test_update_tag_and_succeed(self, client, test_tags, new_tags):
        with current_app.test_request_context(method="POST", json=test_tags[0]):
            response = TagCommandHandler.tag_update(new_tags[0].id)
        assert response.status_code == ExerciseResponse.ok_updated().status_code
        assert TagDatabaseChecker.check_if_name_exist(test_tags[0]["name"], client)

    def test_update_tag_and_fail_because_other_tag_has_same_name(
        self, client, test_tags, new_tags
    ):
        with current_app.test_request_context(method="POST", json=test_tags[1]):
            print("tag[0]:{}\ntag[1]:{}".format(test_tags[0], test_tags[1]))
            response = TagCommandHandler.tag_update(new_tags[0].id)
        assert response.status_code == ExerciseResponse.error_not_found().status_code
        assert TagDatabaseChecker.check_if_name_exist(test_tags[0]["name"], client)

    def test_delete_tag_from_db_and_succeed(self, client, new_tags):
        response = TagCommandHandler.tag_delete(new_tags[0].id)
        assert response.status_code == ExerciseResponse.ok_deleted().status_code
        assert not TagDatabaseChecker.check_if_name_exist(new_tags[0].name, client)

    def test_delete_tag_from_db_and_fail(self, client):
        response = TagCommandHandler.tag_delete("SomeFakeIdOfTag")
        assert response.status_code == ExerciseResponse.error_not_found().status_code
        assert not TagDatabaseChecker.check_if_name_exist(
            "NoSuchTagInBaseTrolololo", client
        )

    def test_create_two_tags_with_same_category_and_unique_names_and_succeed(
        self, client
    ):
        tags = [
            {"name": "tag3", "category": "category1"},
            {"name": "tag4", "category": "category1"},
        ]
        with current_app.test_request_context(method="POST", json=tags[0]):
            response = TagCommandHandler.tag_create()
            print("request 1: {}".format(request.get_json()))
        print("request 1_2: {}".format(request.get_json()))
        with current_app.test_request_context(method="POST", json=tags[1]):
            response = TagCommandHandler.tag_create()
            print("request 2: {}".format(request.get_json()))
        print("request 2_2: {}".format(request.get_json()))
        assert response.status_code == ExerciseResponse.ok_created().status_code
        assert TagDatabaseChecker.check_if_name_exist(tags[0]["name"], client)
        assert TagDatabaseChecker.check_if_name_exist(tags[1]["name"], client)


#     # def create_category_and_success()

#     # def create_category_and_fail_already_exist()


#     # def - create, update, get, get_list - permisions for users

#     # def test_get_exercises_with_tag_and_success()

#     # def test_get_exercises_with_tag_and_fail()
