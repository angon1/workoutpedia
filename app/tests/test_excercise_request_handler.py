from flask import current_app, request
from flask import url_for, json, jsonify
from app.excercises.models import Excercise, Tag
from app.excercises.excercise_request_handler import ExcerciseRequestHandler


class TestExcerciseRequestDispatcher:
    def test_processing_create_request(self, client, test_excercise):
        with current_app.test_request_context(method="POST", json=test_excercise):
            print("\n\nrequest = {}".format(request))
            # ExcerciseRequestHandler.process_create_request()
            ExerciseRequestDispatcher.process_create(request)
        assert client.get("excercises/unittest1/serialized").status_code == 200

    # Dispatcher.ExcerciseHandler.costam.funkja()
    # DispatcherInterface()
    # DisptarchersUtilty() - elemnty wspolne

    # def test_delete_excercise_from_db()

    # def test_add_tag_to_excercise()

    # DispatcherExcerciseRequest
    # dyspozytor.zwaliduj_ten_request_potem_obsluz_ten_request_i_potwierdz_czy_sie_udalo_czy_nie(ten_request)
    # rozdzielacz_zadań

    # ExcerciseRequestHandler.process_nazw

    # Dispatcher.process_request(request, typ danych, rodzaj_requestu)
    # RequestDispatcher.process_request(request, excercise, create)
    # def test_excercise_dict(self, client, new_excercise):
    #     """
    #     GIVEN an Excercise model and excercise dictionary
    #     WHEN GET is send to excercise url
    #     THEN check if proper excercise dictionary is returned
    #     """
    #     excerciseDict = new_excercise.asDict()
    #     data = json.loads(client.get("excercises/unittest1/serialized").get_data())
    #     print(data)
    #     assert data == excerciseDict

    # def test_excercise_add_post(self, client, test_excercise):
    #     """
    #     GIVEN a test excercise data
    #     WHEN post  JSONified excercise data to excercise_add url
    #     THEN check if excercise is added to db
    #     """
    #     excerciseJson = json.dumps(test_excercise)
    #     print(excerciseJson)
    #     response = client.post(
    #         "excercises/create",
    #         data=excerciseJson,
    #         content_type="application/json",
    #     )
    #     data = json.loads(response.get_data(as_text=True))
    #     print(data)
    #     assert response.status_code == 200
    #     assert data["message"] == "Succesfuly added to base"

    # def test_excercise_update_post(self, client, new_excercise, test_excercise):
    #     """
    #     GIVEN a test excercise data
    #     WHEN post  JSONified excercise data to excercise_add url
    #     THEN check if excercise is added to db
    #     """
    #     updateUrl = "excercises/{}/update".format(new_excercise.id)
    #     excerciseJson = json.dumps(test_excercise)
    #     print(updateUrl)
    #     response = client.post(
    #         updateUrl,
    #         data=excerciseJson,
    #         content_type="application/json",
    #     )
    #     data = json.loads(response.get_data(as_text=True))
    #     print(data)
    #     assert response.status_code == 200
    #     assert data["message"] == "Succesfuly updated excercise in base"

    # def test_excercise_delete_post(self, client, new_excercise, test_excercise):
    #     """
    #     GIVEN a test excercise data
    #     WHEN post  JSONified excercise data to excercise_add url
    #     THEN check if excercise is added to db
    #     """
    #     deleteUrl = "excercises/{}/delete".format(new_excercise.id)
    #     excerciseJson = json.dumps(test_excercise)
    #     print(deleteUrl)
    #     response = client.post(
    #         deleteUrl,
    #         data=excerciseJson,
    #         content_type="application/json",
    #     )
    #     data = json.loads(response.get_data(as_text=True))
    #     print(data)
    #     assert response.status_code == 200
    #     assert data["message"] == "Excercise deleted"

    # def test_excercise_delete_not_in_base_post(self, client, test_excercise):
    #     """
    #     GIVEN a test excercise data
    #     WHEN post  JSONified excercise data to excercise_add url
    #     THEN check if excercise is added to db
    #     """
    #     deleteUrl = "excercises/123/delete"
    #     excerciseJson = json.dumps(test_excercise)
    #     print(deleteUrl)
    #     response = client.post(
    #         deleteUrl,
    #         data=excerciseJson,
    #         content_type="application/json",
    #     )
    #     data = json.loads(response.get_data(as_text=True))
    #     print(data)
    #     assert response.status_code == 400
    #     assert data["message"] == "Excercise not found"
