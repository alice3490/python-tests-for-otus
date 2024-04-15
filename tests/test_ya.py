import requests
from conftest import base_url, status_code


def test_valid(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code


def test_invalid(base_url, status_code):
    response = requests.get(f"{base_url}/ertert")
    assert response.status_code == 404
