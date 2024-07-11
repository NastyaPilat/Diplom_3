from pages.base_page import BasePage
from locators import base_page_locators, home_page_locators, login_page_locators
from constants import CREDENTIALS, HOME_PAGE_URL, LOGIN_PAGE_URL


class FeedPage(BasePage):

    def click_order(self):
        self.find_element(base_page_locators.ORDER_ID).click()
