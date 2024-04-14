import requests


class YandexClient:
    def __init__(self,
                 base_url,
                 auth_token):
        self.session = requests.Session()
        self.session.headers = {"Authorization": f"{auth_token}",
                                "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url
