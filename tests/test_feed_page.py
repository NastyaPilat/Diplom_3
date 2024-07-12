import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import HOME_PAGE_URL, FEED_PAGE_URL
from locators import base_page_locators, profile_page_locators, feed_page_locators
from pages.home_page import HomePage
from pages.feed_page import FeedPage


class TestFeedPage():

    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, driver: WebDriver):
        feed_page = FeedPage(driver)
        feed_page.go_to(FEED_PAGE_URL)
        feed_page.wait_for_element_to_be_visible(base_page_locators.ORDER_ID)
        feed_page.click_order()
        assert EC.visibility_of_element_located(
            base_page_locators.OPENED_MODAL)(driver)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_displayed_in_feed(self, driver: WebDriver):
        home_page = HomePage(driver)
        home_page.go_to(HOME_PAGE_URL)
        home_page.login()
        home_page.make_order()
        home_page.click_element(base_page_locators.PROFILE_BTN)
        home_page.wait_for_element_to_be_clickable(
            profile_page_locators.HISTORY_BTN)
        home_page.click_element(profile_page_locators.HISTORY_BTN)
        home_page.wait_for_element_to_be_visible(base_page_locators.ORDER_ID)
        order_id_from_history = home_page.find_elements(
            base_page_locators.ORDER_ID)[-1].text
        home_page.go_to(FEED_PAGE_URL)
        home_page.wait_for_element_to_be_visible(base_page_locators.ORDER_ID)
        order_id_from_feed = home_page.find_element(
            base_page_locators.ORDER_ID).text
        assert order_id_from_history == order_id_from_feed

    @allure.title('При создании нового заказа счётчик {counter_locator} увеличивается')
    @pytest.mark.parametrize('counter_locator', [feed_page_locators.ALL_TIME_ORDERS_COUNTER, feed_page_locators.TODAY_ORDERS_COUNTER])
    def test_all_time_orders_counter(self, driver: WebDriver, counter_locator):
        home_page = HomePage(driver)
        home_page.go_to(FEED_PAGE_URL)
        home_page.wait_for_element_to_be_visible(counter_locator)
        value_before = home_page.find_element(counter_locator).text
        home_page.go_to(HOME_PAGE_URL)
        home_page.login()
        home_page.make_order()
        home_page.go_to(FEED_PAGE_URL)
        home_page.wait_for_element_to_be_visible(counter_locator)
        value_after = home_page.find_element(counter_locator).text
        assert value_before != value_after

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_progress_list(self, driver: WebDriver):
        home_page = HomePage(driver)
        home_page.go_to(HOME_PAGE_URL)
        home_page.login()
        home_page.make_order()
        home_page.go_to(FEED_PAGE_URL)
        home_page.wait_for_element_to_be_visible(
            feed_page_locators.ORDER_ID_IN_PROGRESS)
        initial_text = home_page.find_element(
            feed_page_locators.ORDER_ID_IN_PROGRESS).text
        WebDriverWait(driver, 5).until(lambda _: home_page.find_element(
            feed_page_locators.ORDER_ID_IN_PROGRESS).text != initial_text)
        assert home_page.find_element(
            feed_page_locators.ORDER_ID_IN_PROGRESS).text != initial_text
