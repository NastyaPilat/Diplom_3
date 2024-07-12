import allure
from locators import home_page_locators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('click_constructor_btn')
    def click_constructor_btn(self):
        self.find_element(home_page_locators.CONSTRUCTOR_BTN).click()

    @allure.step('click_feed_btn')
    def click_feed_btn(self):
        self.find_element(home_page_locators.FEED_BTN).click()

    @allure.step('click_ingredient')
    def click_ingredient(self):
        self.find_element(home_page_locators.INGREDIENT).click()

    @allure.step('make_order')
    def make_order(self):
        self.wait_for_element_to_be_clickable(
            home_page_locators.INGREDIENT)
        self.drag_and_drop(
            home_page_locators.INGREDIENT, home_page_locators.CONSTRUCTOR_AREA)
        self.click_element(home_page_locators.MAKE_ORDER_BTN)
        self.close_modal()
