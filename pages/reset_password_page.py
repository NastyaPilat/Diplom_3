import allure
from locators import reset_password_page_locators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('click_password_visibility_btn')
    def click_password_visibility_btn(self):
        self.find_element(
            reset_password_page_locators.PASSWORD_VISIBILITY_BTN).click()
