import json
import requests
from http import HTTPStatus


URL = "http://localhost/api/holidays"


def get_holidays():
    res = requests.get(URL)
    if res.status_code == HTTPStatus.OK:
        return res.json()
    return None
