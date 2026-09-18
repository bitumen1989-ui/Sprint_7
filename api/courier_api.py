import allure
import requests

from urls import BASE_URL, COURIER_CREATE, COURIER_LOGIN, COURIER_DELETE


class CourierApi:
    """Класс для работы с ручками курьера."""

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    @allure.step("Создание курьера: {payload}")
    def create(self, payload: dict) -> requests.Response:
        """POST /api/v1/courier — создание курьера."""
        return requests.post(
            f"{self.base_url}{COURIER_CREATE}",
            data=payload,
        )

    @allure.step("Авторизация курьера: {payload}")
    def login(self, payload: dict) -> requests.Response:
        """POST /api/v1/courier/login — авторизация курьера."""
        return requests.post(
            f"{self.base_url}{COURIER_LOGIN}",
            data=payload,
        )

    @allure.step("Удаление курьера по id: {courier_id}")
    def delete(self, courier_id) -> requests.Response:
        """DELETE /api/v1/courier/{id} — удаление курьера по id."""
        return requests.delete(
            f"{self.base_url}{COURIER_DELETE}/{courier_id}",
        )