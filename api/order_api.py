import allure
import requests

from urls import BASE_URL, ORDERS_CREATE, ORDERS_LIST, ORDERS_CANCEL


class OrderApi:
    """Класс для работы с ручками заказа."""

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    @allure.step("Создание заказа: {payload}")
    def create(self, payload: dict) -> requests.Response:
        """POST /api/v1/orders — создание заказа."""
        return requests.post(
            f"{self.base_url}{ORDERS_CREATE}",
            json=payload,
        )

    @allure.step("Получение списка заказов с параметрами: {params}")
    def get_list(self, params: dict | None = None) -> requests.Response:
        """GET /api/v1/orders — получение списка заказов."""
        return requests.get(
            f"{self.base_url}{ORDERS_LIST}",
            params=params,
        )

    @allure.step("Отмена заказа по track: {track}")
    def cancel(self, track) -> requests.Response:
        """
        PUT /api/v1/orders/cancel — отмена заказа по track.
        track передаётся в query-параметрах, а не в теле —
        в документации по этому поводу ошибка (см. задание).
        """
        return requests.put(
            f"{self.base_url}{ORDERS_CANCEL}",
            params={"track": track},
        )