BASE_URL = "https://qa-scooter.praktikum-services.ru"
API_PREFIX = "/api/v1"

# Ручки курьера
COURIER_CREATE = f"{API_PREFIX}/courier"
COURIER_LOGIN = f"{API_PREFIX}/courier/login"
COURIER_DELETE = f"{API_PREFIX}/courier"  # + /{id}

# Ручки заказа
ORDERS_CREATE = f"{API_PREFIX}/orders"
ORDERS_LIST = f"{API_PREFIX}/orders"
ORDERS_CANCEL = f"{API_PREFIX}/orders/cancel"