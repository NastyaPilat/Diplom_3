import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from constants import FORGOT_PASSWORD_URL
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from locators import reset_password_page_locators


class TestResetPasswordPage():

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_toggle_password_visibility(self, driver: WebDriver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to(FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email()
        forgot_password_page.click_recovery_btn()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_element_to_be_clickable(
            reset_password_page_locators.PASSWORD_VISIBILITY_BTN)
        reset_password_page.click_password_visibility_btn()
        assert EC.visibility_of_element_located(
            reset_password_page_locators.PASSWORD_INPUT_CONTAINER_ACTIVE)(driver)
