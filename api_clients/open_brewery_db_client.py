import requests


class OpenBreweryClient:

    def __init__(self,
                 base_url="https://api.openbrewerydb.org",
                 auth_token="special-key"):
        self.session = requests.Session()
        self.session.headers = {"Authorization": f"{auth_token}",
                                "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_breweries(self, per_page):
        response = self.session.get(url=f"{self.base_url}/v1/breweries?per_page={per_page}")
        return response

    def get_brewery_by_id(self, obdb_id):
        response = self.session.get(url=f"{self.base_url}/v1/breweries/{obdb_id}")
        return response

    def get_breweries_by_ids(self, ids, per_page):
        str_ids = ''
        for id in ids:
            if len(ids) > 1:
                str_ids += id
                str_ids += ','
            else:
                str_ids += id
        response = self.session.get(url=f"{self.base_url}/v1/breweries/?by_ids={str_ids}&per_page={per_page}")
        return response

    def get_breweries_by_type(self, type, per_page):
        str_type = ''
        str_type += type
        response = self.session.get(url=f"{self.base_url}/v1/breweries/?by_type={str_type}&per_page={per_page}")
        return response

    def get_metadata(self, params):
        response = self.session.get(url=f"{self.base_url}/v1/breweries/meta?{params}")
        return response
