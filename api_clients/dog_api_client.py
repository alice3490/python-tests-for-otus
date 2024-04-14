import requests
from schemas.dog_api_schemas import list_all_breeds_schema

class DogApiClient:
    def __init__(self,
                 base_url="https://dog.ceo/api",
                 auth_token="special-key"):
        self.session = requests.Session()
        self.session.headers = {"Authorization": f"{auth_token}",
                                "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def list_all_breeds(self):
        response = self.session.get(url=f"{self.base_url}/breeds/list/all")
        return response

    def random_image(self, count):
        response = self.session.get(url=f"{self.base_url}/breeds/image/random/{count}")
        return response

    def by_breed(self, breed):
        response = self.session.get(url=f"{self.base_url}/breed/{breed}/images")
        return response

    def by_sub_breed(self, breed):
        response = self.session.get(url=f"{self.base_url}/breed/{breed}/list")
        return response

    def breeds_list(self, breed):
        response = self.session.get(url=f"{self.base_url}/breed/{breed}/images/random")
        return response
