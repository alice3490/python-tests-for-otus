import pytest
from schemas.dog_api_schemas import list_all_breeds_schema, by_sub_breed_list_schema
from jsonschema import validate

from type_checkers import check_type_for_get_random_image


class TestDogApi:
    def test_list_all_breeds(self, dog_api_client):
        response = dog_api_client.list_all_breeds()
        assert response.status_code == 200
        json_response = response.json()
        validate(instance=json_response, schema=list_all_breeds_schema)

    @pytest.mark.parametrize("count", [1, 2, 49, 50, 51, 0])
    def test_random_image(self, dog_api_client, count):
        response = dog_api_client.random_image(count=count)
        assert response.status_code == 200
        json_response = response.json()
        if count > 50:
            assert len(json_response.get("message")) == 50
        elif count == 0:
            assert len(json_response.get("message")) == 1
        else:
            assert len(json_response.get("message")) == count
        assert json_response.get("status") == "success"
        check_type_for_get_random_image(response=json_response)

    @pytest.mark.parametrize("breed, status_code", [("terrier", 200), ("unknown", 404)])
    def test_by_breed(self, dog_api_client, breed, status_code):
        response = dog_api_client.by_breed(breed=breed)
        assert response.status_code == status_code
        json_response = response.json()
        if status_code == 200:
            for url in json_response['message']:
                assert f"https://images.dog.ceo/breeds/{breed}" in url
        if status_code == 404:
            assert json_response["status"] == "error"
            assert json_response["message"] == "Breed not found (master breed does not exist)"

    @pytest.mark.parametrize("breed", ["bulldog", "collie", "chihuahua"])
    def test_by_sub_breed(self, dog_api_client, breed):
        response = dog_api_client.by_sub_breed(breed=breed)
        assert response.status_code == 200
        json_response = response.json()
        validate(instance=json_response, schema=by_sub_breed_list_schema)
        if breed == "bulldog":
            assert len(json_response["message"]) == 3
        elif breed == "collie":
            assert len(json_response["message"]) == 1
        else:
            assert json_response['message'] == []

    @pytest.mark.parametrize("breed, status_code", [("terrier", 200), ("unknown", 404)])
    def test_breeds_list(self, dog_api_client, breed, status_code):
        response = dog_api_client.breeds_list(breed=breed)
        assert response.status_code == status_code
