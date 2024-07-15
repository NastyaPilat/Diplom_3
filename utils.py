import requests
import random
import string
import allure
from endpoints import REGISTER_URL


def generate_random_user():
    email = ''.join(random.choices(string.ascii_letters +
                    string.digits, k=8)) + '@yandex.ru'
    password = ''.join(random.choices(
        string.ascii_letters + string.digits, k=8))
    name = ''.join(random.choices(string.ascii_letters, k=8))
    return email, password, name


@allure.step('Зарегистрировать пользователя')
def register_user():
    email, password, name = generate_random_user()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    try:
        response = requests.post(REGISTER_URL, json=payload)
        if response.status_code == 200:
            return payload
        return False
    except Exception as e:
        print(f"Error registering user: {str(e)}")
        return False
