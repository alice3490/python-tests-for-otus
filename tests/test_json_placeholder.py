import random

import pytest

from query_params import create_resource, update_resource

from type_checkers import check_type_for_get_resource


class TestJsonPlaceholder:
    @pytest.mark.parametrize("id, status_code", [(1, 200), (2, 200), (0, 404)])
    def test_get_resource(self, json_placeholder_client, id, status_code):
        response = json_placeholder_client.get_resource(id=id)
        assert response.status_code == status_code
        json_response = response.json()
        if response.status_code == 200:
            check_type_for_get_resource(response=json_response)

    def test_create_new_resource(self, json_placeholder_client):
        user_id = random.randint(1, 100)
        query = create_resource(user_id=user_id, title="new", body="post")
        response = json_placeholder_client.create_resource(query=query)
        assert response.status_code == 201

    def test_update_resource(self, json_placeholder_client):
        query = update_resource(user_id=3, body="new_body", title="update", id=7)
        response = json_placeholder_client.update_resource(id=7, query=query)
        json_response = response.json()
        print(json_response)

