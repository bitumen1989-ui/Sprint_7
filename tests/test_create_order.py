import allure
import pytest


@allure.feature("Создание заказа")
class TestCreateOrder:
    """Тесты на ручку POST /api/v1/orders."""

    @pytest.mark.parametrize(
        "color",
        [
            pytest.param(["BLACK"], id="BLACK"),
            pytest.param(["GREY"], id="GREY"),
            pytest.param(["BLACK", "GREY"], id="BLACK_AND_GREY"),
            pytest.param(None, id="NO_COLOR"),
        ],
    )
    @allure.title("Создание заказа с цветом: {color}")
    def test_create_order_with_color(self, order_api, color):
        """Заказ создаётся с любым набором цветов. В теле есть track."""
        payload = {
            "firstName": "Test",
            "lastName": "Tester",
            "address": "Moscow, Test street, 1",
            "metroStation": 1,
            "phone": "+79999999999",
            "rentTime": 1,
            "deliveryDate": "2026-01-01",
            "comment": "test order",
        }
        if color is not None:
            payload["color"] = color

        response = order_api.create(payload)

        assert response.status_code == 201
        assert "track" in response.json()