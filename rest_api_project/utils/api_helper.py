import requests
from rest_api_project.utils.allure_attach import response_logging, response_attaching


def api_request(base_api_url, endpoint, method, data=None, params=None):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method, url, data=data, params=params)
    response_logging(response)
    response_attaching(response)
    return response
