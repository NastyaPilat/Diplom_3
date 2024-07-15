import allure
from locators import base_page_locators, forgot_password_page_locators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('enter_email')
    def enter_email(self):
        input = self.find_element(base_page_locators.INPUT)
        input.send_keys('email@yandex.com')

    @allure.step('click_recovery_btn')
    def click_recovery_btn(self):
        self.find_element(forgot_password_page_locators.RECOVERY_BTN).click()
