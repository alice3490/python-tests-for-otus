import random

import pytest
from pydantic import BaseModel


class JsonPlaceholder(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class PatchResource(BaseModel):
    id: int
    title: str


class TestJsonPlaceholder:
    @pytest.mark.parametrize("id, status_code", [(1, 200), (2, 200), (0, 404)])
    def test_get_resource(self, json_placeholder_client, id, status_code):
        response = json_placeholder_client.get_resource(id=id)
        assert response.status_code == status_code
        json_response = response.json()
        if response.status_code == 200:
            JsonPlaceholder.parse_obj(json_response)

    @pytest.mark.parametrize("title, body", [("resource_1", "create_body_1"),
                                             ("resource_2", "create_body_2")])
    def test_create_new_resource(self, json_placeholder_client, title, body):
        user_id = random.randint(1, 100)
        id = random.randint(1, 100)
        title = "new_resource"
        body = "create_body"
        json = {
            "id": id,
            "title": title,
            "body": body,
            "userId": user_id,
        }
        response = json_placeholder_client.create_resource(json=json)
        json_response = response.json()
        JsonPlaceholder.parse_obj(json_response)
        assert json_response["title"] == title
        assert json_response["body"] == body
        assert json_response["userId"] == user_id

    def test_update_resource(self, json_placeholder_client):
        list_resources = json_placeholder_client.get_all_resources().json()
        ids = [res['id'] for res in list_resources]
        id = random.choice(ids)
        user_id = random.randint(1, 100)
        title = "updated_resource"
        body = "updated_body"
        json = {
            "id": id,
            "title": title,
            "body": body,
            "userId": user_id,
        }
        response = json_placeholder_client.update_resource(id=id, json=json)
        json_response = response.json()
        JsonPlaceholder.parse_obj(json_response)
        assert json_response["title"] == title
        assert json_response["body"] == body
        assert json_response["userId"] == user_id

    def test_patch_resource(self, json_placeholder_client):
        list_resources = json_placeholder_client.get_all_resources().json()
        ids = [res['id'] for res in list_resources]
        id = random.choice(ids)
        title = "patch_title"
        json = {
            "title": title
        }
        response = json_placeholder_client.update_resource(id=id, json=json)
        json_response = response.json()
        PatchResource.parse_obj(json_response)
        assert json_response["title"] == title

    def test_delete_resource(self, json_placeholder_client):
        list_resources = json_placeholder_client.get_all_resources().json()
        ids = [res['id'] for res in list_resources]
        id = random.choice(ids)
        response = json_placeholder_client.delete_resource(id=id)
        json_response = response.json()
        JsonPlaceholder.parse_obj(json_response)
