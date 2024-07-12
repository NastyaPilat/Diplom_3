import allure
from locators import base_page_locators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('click_order')
    def click_order(self):
        self.find_element(base_page_locators.ORDER_ID).click()
