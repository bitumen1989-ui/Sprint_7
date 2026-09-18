import pytest

from api.courier_api import CourierApi
from data_generator import generate_courier_data


@pytest.fixture
def courier():
    """
    Создаёт курьера, отдаёт тесту api, данные и response от создания,
    удаляет курьера после теста.
    """
    api = CourierApi()
    data = generate_courier_data()
    response = api.create(data)

    yield {
        "api": api,
        "data": data,
        "response": response,
    }

    login_response = api.login({
        "login": data["login"],
        "password": data["password"],
    })
    api.delete(login_response.json()["id"])