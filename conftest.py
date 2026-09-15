import pytest

from api.courier_api import CourierApi
from api.order_api import OrderApi
from data_generator import generate_courier_data
from urls import BASE_URL


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def courier_api() -> CourierApi:
    return CourierApi()


@pytest.fixture
def order_api() -> OrderApi:
    return OrderApi()


@pytest.fixture
def courier(courier_api):
    """
    Создаёт курьера, отдаёт тесту его данные, удаляет после теста.
    Удаление — по id, который получаем через логин.
    """
    data = generate_courier_data()
    courier_api.create(data)

    yield data

    # teardown: логинимся, получаем id, удаляем
    login_response = courier_api.login({
        "login": data["login"],
        "password": data["password"],
    })
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        courier_api.delete(courier_id)


@pytest.fixture
def order(order_api):
    """
    Создаёт заказ, отдаёт тесту payload/track/response, отменяет после теста.
    Цвет по умолчанию — BLACK.
    """
    payload = {
        "firstName": "Test",
        "lastName": "Tester",
        "address": "Moscow, Test street, 1",
        "metroStation": 1,
        "phone": "+79999999999",
        "rentTime": 1,
        "deliveryDate": "2026-01-01",
        "comment": "test order",
        "color": ["BLACK"],
    }
    response = order_api.create(payload)
    track = response.json().get("track")

    yield {"payload": payload, "track": track, "response": response}

    # teardown: отменяем заказ по track
    if track:
        order_api.cancel(track)