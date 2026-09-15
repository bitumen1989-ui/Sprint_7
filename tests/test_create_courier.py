import allure
import pytest

from data_generator import generate_courier_data


@allure.feature("Создание курьера")
class TestCreateCourier:
    """Тесты на ручку POST /api/v1/courier."""

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_api):
        """Курьера можно создать. Возвращается 201 и {"ok": true}."""
        data = generate_courier_data()

        response = courier_api.create(data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # teardown
        login_response = courier_api.login({
            "login": data["login"],
            "password": data["password"],
        })
        if login_response.status_code == 200:
            courier_api.delete(login_response.json()["id"])

    @allure.title("Ошибка при создании двух одинаковых курьеров")
    def test_create_two_identical_couriers_returns_error(self, courier_api, courier):
        """Нельзя создать двух одинаковых курьеров — возвращается 409."""
        duplicate_data = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"],
        }

        response = courier_api.create(duplicate_data)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_create_courier_with_existing_login_returns_error(self, courier_api, courier):
        """Если логин уже есть — возвращается 409."""
        data = generate_courier_data()
        data["login"] = courier["login"]

        response = courier_api.create(data)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Ошибка при создании курьера без поля: {missing_field}")
    def test_create_courier_without_required_field_returns_error(
        self, courier_api, missing_field
    ):
        """Если одного из обязательных полей нет — возвращается 400."""
        data = generate_courier_data()
        data.pop(missing_field)

        response = courier_api.create(data)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Успешное создание курьера без firstName")
    def test_create_courier_without_first_name_success(self, courier_api):
        """firstName — необязательное поле, без него курьер создаётся."""
        data = generate_courier_data()
        data.pop("firstName")

        response = courier_api.create(data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # teardown
        login_response = courier_api.login({
            "login": data["login"],
            "password": data["password"],
        })
        if login_response.status_code == 200:
            courier_api.delete(login_response.json()["id"])