import requests
import random
import string
import allure


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
    url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return {
                'email': email,
                'password': password,
                'name': name,
            }
        else:
            return {'success': False}
    except Exception as e:
        print(f"Error registering user: {str(e)}")
        return {'success': False}