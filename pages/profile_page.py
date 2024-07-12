import allure
from locators import profile_page_locators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('click_history_btn')
    def click_history_btn(self):
        self.find_element(profile_page_locators.HISTORY_BTN).click()

    @allure.step('click_signout_btn')
    def click_signout_btn(self):
        self.find_element(profile_page_locators.SIGNOUT_BTN).click()
