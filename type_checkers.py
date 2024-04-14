def check_type_for_get_random_image(response):
    assert type(response["message"]) is list
    assert type(response["status"]) is str

def check_type_for_brewery(brewery_list: list):
    for brewery in brewery_list:
        assert type(brewery['id']) is str
        assert type(brewery['name']) is str
        assert type(brewery['brewery_type']) is str
        assert type(brewery['address_1']) is str or "null"
        assert type(brewery['address_2']) is str or "null"
        assert type(brewery['address_3']) is str or "null"
        assert type(brewery['city']) is str
        assert type(brewery['state_province']) is str
        assert type(brewery['postal_code']) is str
        assert type(brewery['country']) is str
        # assert type(brewery['longitude']) is str
        # assert type(brewery['latitude']) is str
        assert type(brewery['phone']) is str or "null"
        assert type(brewery['website_url']) is str or "null"
        assert type(brewery['state']) is str
        assert type(brewery['street']) is str or "null"

def check_type_for_get_resource(response):
    assert type(response["id"]) is int
    assert type(response["title"]) is str
    assert type(response["body"]) is str
    assert type(response["userId"]) is int


