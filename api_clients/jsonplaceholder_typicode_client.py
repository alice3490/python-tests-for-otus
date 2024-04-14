import requests


class JsonPlaceholderClient:

    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com",
                 auth_token="special-key"):
        self.session = requests.Session()
        self.session.headers = {"Authorization": f"{auth_token}",
                                "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_resource(self, id):
        response = self.session.get(url=f"{self.base_url}/posts/{id}")
        return response

    def get_all_resources(self):
        response = self.session.get(url=f"{self.base_url}/posts")
        return response

    def create_resource(self, query):
        response = self.session.post(url=f"{self.base_url}/posts", params=query)
        return response

    def update_resource(self, id, query):
        response = self.session.put(url=f"{self.base_url}/posts/{id}", params=query)
        return response

    def patch_resource(self, id, query):
        response = self.session.get(url=f"{self.base_url}/posts/{id}", params=query)
        return response

    def delete_resource(self, id):
        response = self.session.get(url=f"{self.base_url}/posts/{id}", params={"method": "DELETE"})
        return response
