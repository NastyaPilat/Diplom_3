import allure
from endpoints import LOGIN_PAGE_URL, FORGOT_PASSWORD_PAGE_URL
from pages.login_page import LoginPage


class TestLoginPage():

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery_page(self, login_page: LoginPage):
        login_page.go_to(LOGIN_PAGE_URL)
        login_page.click_recovery_btn()
        assert login_page.get_current_url() == FORGOT_PASSWORD_PAGE_URL
