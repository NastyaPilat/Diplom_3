import allure
from locators import login_page_locators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('click_recovery_btn')
    def click_recovery_btn(self):
        self.find_element(login_page_locators.RECOVERY_BTN).click()
