import allure
import pytest
from endpoints import HOME_PAGE_URL, FEED_PAGE_URL
from locators import base_page_locators, profile_page_locators, feed_page_locators
from pages.home_page import HomePage
from pages.feed_page import FeedPage


class TestFeedPage():

    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, feed_page: FeedPage):
        feed_page.go_to(FEED_PAGE_URL)
        feed_page.wait_for_element_to_be_visible(base_page_locators.ORDER_ID)
        feed_page.click_order()
        feed_page.wait_for_element_to_be_visible(
            base_page_locators.ORDER_MODAL)
        assert feed_page.is_element_visible(base_page_locators.ORDER_MODAL)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_displayed_in_feed(self, home_page: HomePage):
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
    def test_all_time_orders_counter(self, home_page: HomePage, counter_locator):
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
    def test_progress_list(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.login()
        home_page.make_order()
        home_page.go_to(FEED_PAGE_URL)
        home_page.wait_for_element_to_be_visible(
            feed_page_locators.ORDER_ID_IN_PROGRESS)
        initial_text = home_page.find_element(
            feed_page_locators.ORDER_ID_IN_PROGRESS).text
        home_page.wait_until(lambda _: home_page.find_element(
            feed_page_locators.ORDER_ID_IN_PROGRESS).text != initial_text, 5)
        assert home_page.find_element(
            feed_page_locators.ORDER_ID_IN_PROGRESS).text != initial_text
