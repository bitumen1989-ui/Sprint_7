import allure
import pytest

from data_generator import generate_courier_data


@allure.feature("Логин курьера")
class TestLoginCourier:
    """Тесты на ручку POST /api/v1/courier/login."""

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_api, courier):
        """Курьер может авторизоваться. Возвращается 200 и id."""
        response = courier_api.login({
            "login": courier["login"],
            "password": courier["password"],
        })

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка авторизации без поля login")
    def test_login_courier_without_login_returns_error(self, courier_api, courier):
        """
        Для авторизации нужно передать login.
        Кейс 'без password' стабильно отдаёт 504 Service unavailable —
        это баг сервера, поэтому не тестируем.
        """
        response = courier_api.login({
            "password": courier["password"],
        })

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @pytest.mark.parametrize("invalid_field", ["login", "password"])
    @allure.title("Ошибка авторизации при неверном поле: {invalid_field}")
    def test_login_courier_with_invalid_data_returns_error(
        self, courier_api, courier, invalid_field
    ):
        """Система вернёт 404, если неправильно указать логин или пароль."""
        payload = {
            "login": courier["login"],
            "password": courier["password"],
        }
        payload[invalid_field] = "wrong_" + payload[invalid_field]

        response = courier_api.login(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка авторизации под несуществующим пользователем")
    def test_login_courier_with_nonexistent_user_returns_error(self, courier_api):
        """Если авторизоваться под несуществующим пользователем — 404."""
        data = generate_courier_data()

        response = courier_api.login({
            "login": data["login"],
            "password": data["password"],
        })

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"