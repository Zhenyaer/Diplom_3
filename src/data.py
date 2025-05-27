import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_user_data():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    username = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": username
    }
    return payload


class ControlText:
    ORDER_STATUS_READY = 'Ваш заказ начали готовить'
    OPEN_POPUP_CLASS = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5'
    CLOSE_POPUP_CLASS = 'Modal_modal__P3_V5'
    STATUS_PASSWORD_FIELD_CLASS = 'input_status_active'
