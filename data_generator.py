import random
import string

import requests

from urls import BASE_URL, COURIER_CREATE


def generate_random_string(length: int) -> str:
    """Генерирует строку из букв нижнего регистра заданной длины."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def generate_courier_data() -> dict:
    """Возвращает словарь с логином, паролем и именем нового курьера."""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }


def register_new_courier_and_return_login_password() -> list:
    """
    Метод регистрации нового курьера.
    Возвращает список [login, password, firstName] при успехе,
    либо пустой список при неудаче.
    """
    login_pass = []

    courier_data = generate_courier_data()
    login = courier_data["login"]
    password = courier_data["password"]
    first_name = courier_data["firstName"]

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    response = requests.post(f"{BASE_URL}{COURIER_CREATE}", data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass