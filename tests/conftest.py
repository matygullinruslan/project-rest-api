import pytest

url = 'https://reqres.in'


@pytest.fixture
def base_url():
    return url
