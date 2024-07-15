import allure
from endpoints import FORGOT_PASSWORD_PAGE_URL, RESET_PASSWORD_PAGE_URL
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPasswordPage():

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_recover(self, forgot_password_page: ForgotPasswordPage):
        forgot_password_page.go_to(FORGOT_PASSWORD_PAGE_URL)
        forgot_password_page.enter_email()
        forgot_password_page.click_recovery_btn()
        forgot_password_page.wait_for_url_to_be(RESET_PASSWORD_PAGE_URL)
        assert forgot_password_page.get_current_url() == RESET_PASSWORD_PAGE_URL
