from jsonschema import validate
from rest_api_project.schemas import schema
import allure
from allure_commons.types import Severity
from rest_api_project.utils.api_helper import api_request


@allure.title("Создание пользователя")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Создание пользователя")
def test_create_user_status_code(base_url):
    endpoint = '/api/users'
    params = {"name": "morpheus", "job": "leader"}
    response = api_request(base_url, endpoint, 'POST', data=params)

    body = response.json()
    assert response.status_code == 201
    assert body["name"] == 'morpheus'
    validate(body, schema.post_users)


@allure.title("Обновление данных пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Обновление данных пользователя")
def test_update_user_status_code(base_url):
    endpoint = '/api/users/2'
    params = {"name": "morpheus", "job": "zion resident"}
    response = api_request(base_url, endpoint, 'PUT', data=params)

    body = response.json()
    assert response.status_code == 200
    assert body["job"] == "zion resident"
    validate(body, schema.update_users)


@allure.title("Получение списка пользователей")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Получение списка пользователей")
def test_get_list_user_status_code(base_url):
    endpoint = '/api/users'
    params = {"images": "2"}
    response = api_request(base_url, endpoint, 'GET', params=params)

    assert response.status_code == 200
    body = response.json()
    validate(body, schema.list_users)


@allure.title("Удаление пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Удаление пользователя")
def test_delete_user_status_code(base_url):
    endpoint = '/api/users/2'
    response = api_request(base_url, endpoint, 'DELETE')

    assert response.status_code == 204
    assert response.text == ""


@allure.title("Запрос не существующего пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Запрос не существующего пользователя")
def test_get_user_not_found_status_code(base_url):
    endpoint = '/api/unknown/23'
    response = api_request(base_url, endpoint, 'GET')

    assert response.status_code == 404
    assert response.json() == {}


@allure.title("Не успешная регистрация пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Не успешная регистрация пользователя")
def test_unsuccessful_registration_user_status_code(base_url):
    endpoint = '/api/register'
    params = {"email": "sydney@fife"}
    response = api_request(base_url, endpoint, 'POST', data=params)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing password"
    validate(body, schema.error_register)


@allure.title("Успешная регистрация пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Успешная регистрация пользователя")
def test_successful_registration_user_status_code(base_url):
    endpoint = '/api/register'
    params = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = api_request(base_url, endpoint, 'POST', data=params)

    body = response.json()
    assert response.status_code == 200
    assert body["id"] == 4
    validate(body, schema.successful_registr)


@allure.title("Регистрация пользователя с некорректным email")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Регистрация пользователя с некорректным email")
def test_invalid_email_registration_user_status_code(base_url):
    endpoint = '/api/register'
    params = {"email": "eve.holt.reqres.in", "password": "pistol"}
    response = api_request(base_url, endpoint, 'POST', data=params)

    assert response.status_code == 400
    assert response.json()["error"] == "Note: Only defined users succeed registration"
