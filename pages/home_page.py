from pages.base_page import BasePage
from locators import base_page_locators, home_page_locators, login_page_locators
from constants import CREDENTIALS, HOME_PAGE_URL, LOGIN_PAGE_URL


class HomePage(BasePage):

    def click_constructor_btn(self):
        self.find_element(home_page_locators.CONSTRUCTOR_BTN).click()

    def click_feed_btn(self):
        self.find_element(home_page_locators.FEED_BTN).click()

    def click_ingredient(self):
        self.find_element(home_page_locators.INGREDIENT).click()

    def login(self):
        self.find_element(home_page_locators.LOGIN_BTN).click()
        self.wait_for_url_to_be(LOGIN_PAGE_URL)
        [input_email, input_password] = self.find_elements(
            base_page_locators.INPUT)
        input_email.send_keys(CREDENTIALS["email"])
        input_password.send_keys(CREDENTIALS["password"])
        self.find_element(login_page_locators.LOGIN_BTN).click()
        self.wait_for_url_to_be(HOME_PAGE_URL)

    def make_order(self):
        self.wait_for_element_to_be_clickable(
            home_page_locators.INGREDIENT)
        self.drag_and_drop(
            home_page_locators.INGREDIENT, home_page_locators.CONSTRUCTOR_AREA)
        self.click_element(home_page_locators.MAKE_ORDER_BTN)
        self.close_modal()
