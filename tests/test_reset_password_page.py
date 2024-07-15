import allure
from endpoints import FORGOT_PASSWORD_PAGE_URL
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from locators import reset_password_page_locators


class TestResetPasswordPage():

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_toggle_password_visibility(self, forgot_password_page: ForgotPasswordPage, reset_password_page: ResetPasswordPage):
        forgot_password_page.go_to(FORGOT_PASSWORD_PAGE_URL)
        forgot_password_page.enter_email()
        forgot_password_page.click_recovery_btn()
        reset_password_page.wait_for_element_to_be_clickable(
            reset_password_page_locators.PASSWORD_VISIBILITY_BTN)
        reset_password_page.click_password_visibility_btn()
        assert reset_password_page.is_element_visible(
            reset_password_page_locators.PASSWORD_INPUT_CONTAINER_ACTIVE)
