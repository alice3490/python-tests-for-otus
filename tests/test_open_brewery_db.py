import random
import uuid

import pytest
from type_checkers import check_type_for_brewery
from conftest import open_brewery_client
from constants import BreweryType
from jsonschema import validate
from schemas.open_brewery_schemas import get_meta_schema


class TestOpenBreweryDB:

    @pytest.mark.parametrize("count", [1, 2, 5])
    def test_list_breweries(self, open_brewery_client, count):
        response = open_brewery_client.get_list_breweries(per_page=count)
        assert response.status_code == 200
        json_response = response.json()
        check_type_for_brewery(json_response)

    def test_get_brewery_by_id_valid(self, open_brewery_client):
        breweries_list = open_brewery_client.get_list_breweries(per_page=20).json()
        brewery_id = random.choice(breweries_list)['id']
        response = open_brewery_client.get_brewery_by_id(obdb_id=brewery_id)
        assert response.status_code == 200
        json_response = response.json()
        check_type_for_brewery([json_response])

    def test_get_brewery_by_id_invalid(self, open_brewery_client):
        brewery_id = uuid.uuid4()
        response = open_brewery_client.get_brewery_by_id(obdb_id=brewery_id)
        assert response.status_code == 404
        json_response = response.json()
        assert "Couldn't find Brewery" in json_response["message"]

    @pytest.mark.parametrize("count", [1, 2, 5])
    def test_get_breweries_by_ids_valid(self, open_brewery_client, count):
        breweries_list = open_brewery_client.get_list_breweries(per_page=count).json()
        ids = []
        for i in range(count):
            ids.append(breweries_list[i - 1]["id"])
        response = open_brewery_client.get_breweries_by_ids(ids=ids, per_page=count)
        assert response.status_code == 200
        json_response = response.json()
        assert len(json_response) == count
        check_type_for_brewery(json_response)

    def test_get_breweries_by_ids_invalid(self, open_brewery_client):
        ids = [str(uuid.uuid4())]
        response = open_brewery_client.get_breweries_by_ids(ids=ids, per_page=1)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response == []

    @pytest.mark.parametrize("count", [1, 2, 5])
    def test_get_breweries_by_type_valid(self, open_brewery_client, count):
        type = random.choice(list(BreweryType))
        response = open_brewery_client.get_breweries_by_type(type=type, per_page=count)
        assert response.status_code == 200
        json_response = response.json()
        check_type_for_brewery(json_response)

    def test_get_breweries_by_type_invalid(self, open_brewery_client):
        type = "invalid_type"
        response = open_brewery_client.get_breweries_by_type(type=type, per_page=1)
        assert response.status_code == 400

    @pytest.mark.parametrize("filter", ['by_type=large', 'by_country=united_states'])
    def test_get_breweries_metadata(self, open_brewery_client, filter):
        str_params = ''
        str_params += filter
        response = open_brewery_client.get_metadata(params=str_params)
        assert response.status_code == 200
        json_response = response.json()
        validate(instance=json_response, schema=get_meta_schema)





