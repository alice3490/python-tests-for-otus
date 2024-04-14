import pytest

from api_clients.dog_api_client import DogApiClient
from api_clients.jsonplaceholder_typicode_client import JsonPlaceholderClient
from api_clients.open_brewery_db_client import OpenBreweryClient


@pytest.fixture(scope="session")
def dog_api_client():
    client = DogApiClient()
    return client


@pytest.fixture(scope="session")
def open_brewery_client():
    client = OpenBreweryClient()
    return client


@pytest.fixture(scope="session")
def json_placeholder_client():
    client = JsonPlaceholderClient()
    return client


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def status_code(request):
    return request.config.getoption("status_code")
