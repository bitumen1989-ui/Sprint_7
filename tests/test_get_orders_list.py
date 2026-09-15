import allure


@allure.feature("Список заказов")
class TestGetOrdersList:
    """Тесты на ручку GET /api/v1/orders."""

    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders(self, order_api):
        """В тело ответа возвращается список заказов."""
        response = order_api.get_list()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)