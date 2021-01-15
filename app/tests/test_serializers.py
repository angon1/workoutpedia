from flask import current_app
from flask import url_for, json, jsonify
from app.excercises.models import Excercise, Tag


class TestSerializers:
    def test_serialized_excercise_get(self, client, new_excercise):
        assert client.get("excercises/unittest1/serialized").status_code == 200

    def test_excercise_dict(self, client, new_excercise):
        """
        GIVEN a Excercise model and excercise dictionary
        WHEN GET is send to excercise url
        THEN check if proper excercise dictionary is returned
        """
        excerciseDict = new_excercise.asDict()
        data = json.loads(client.get("excercises/unittest1/serialized").get_data())
        print(data)
        assert data == excerciseDict

    def test_excercise_add_post(self, client, test_excercise):
        """
        GIVEN a test excercise data
        WHEN post  JSONified excercise data to excercise_add url
        THEN check if excercise is added to db
        """
        excerciseJson = json.dumps(test_excercise)
        print(excerciseJson)
        response = client.post(
            "excercises/create",
            data=excerciseJson,
            content_type="application/json",
        )
        data = json.loads(response.get_data(as_text=True))
        print(data)
        assert response.status_code == 200
        assert data["message"] == "Succesfuly added to base"

    def test_excercise_update_post(self, client, new_excercise, test_excercise):
        """
        GIVEN a test excercise data
        WHEN post  JSONified excercise data to excercise_add url
        THEN check if excercise is added to db
        """
        updateUrl = "excercises/{}/update".format(new_excercise.id)
        excerciseJson = json.dumps(test_excercise)
        print(updateUrl)
        response = client.post(
            updateUrl,
            data=excerciseJson,
            content_type="application/json",
        )
        data = json.loads(response.get_data(as_text=True))
        print(data)
        assert response.status_code == 200
        assert data["message"] == "Succesfuly updated excercise in base"

    def test_excercise_delete_post(self, client, new_excercise, test_excercise):
        """
        GIVEN a test excercise data
        WHEN post  JSONified excercise data to excercise_add url
        THEN check if excercise is added to db
        """
        deleteUrl = "excercises/{}/serialized/delete".format(new_excercise.id)
        excerciseJson = json.dumps(test_excercise)
        print(deleteUrl)
        response = client.post(
            deleteUrl,
            data=excerciseJson,
            content_type="application/json",
        )
        data = json.loads(response.get_data(as_text=True))
        print(data)
        assert response.status_code == 200
        assert data["message"] == "Excercise deleted"

    def test_excercise_delete_not_in_base_post(self, client, test_excercise):
        """
        GIVEN a test excercise data
        WHEN post  JSONified excercise data to excercise_add url
        THEN check if excercise is added to db
        """
        deleteUrl = "excercises/123/serialized/delete"
        excerciseJson = json.dumps(test_excercise)
        print(deleteUrl)
        response = client.post(
            deleteUrl,
            data=excerciseJson,
            content_type="application/json",
        )
        data = json.loads(response.get_data(as_text=True))
        print(data)
        assert response.status_code == 400
        assert data["message"] == "Excercise not found"

    # def test_tags_dict(self, client, new_tags):
    #     """
    #     GIVEN a Excercise model and excercise dictionary
    #     WHEN GET is send to excercise url
    #     THEN check if proper excercise dictionary is returned
    #     """
    #     tagsDict = []
    #     data = json.loads(client.get("tags/serialized").get_data())
    #     print(data)
    #     assert data == tagsDict
