from pkginfo.commandline import JSON


def create_resource(user_id, title, body):
    request_params = {
        "method": 'POST',
        "body": {
            "title": title,
            "body": body,
            "userId": user_id,
        },
        "headers": {
            'Content-type': 'application/json; charset=UTF-8',
        },
    }
    return request_params

def update_resource(id, title, body, user_id):
    request_params = {
        "method": 'PUT',
        "body": {
            "id": 1,
            "title": 'foo',
            "body": 'bar',
            "userId": 1,
        },
        "headers": {
            'Content-type': 'application/json; charset=UTF-8',
        },
    }
    return request_params
