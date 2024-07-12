import allure
from selenium.webdriver.remote.webdriver import WebDriver
from constants import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPasswordPage():

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_recover(self, driver: WebDriver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to(FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email()
        forgot_password_page.click_recovery_btn()
        forgot_password_page.wait_for_url_to_be(RESET_PASSWORD_URL)
        assert forgot_password_page.get_current_url() == RESET_PASSWORD_URL
