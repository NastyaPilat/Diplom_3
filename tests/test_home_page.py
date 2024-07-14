import allure
from endpoints import HOME_PAGE_URL, FEED_PAGE_URL, LOGIN_PAGE_URL
from pages.home_page import HomePage
from locators import base_page_locators, home_page_locators


class TestHomePage():

    @allure.title('Переход по клику на «Конструктор»')
    def test_constructor_btn(self, home_page: HomePage):
        home_page.go_to(FEED_PAGE_URL)
        home_page.click_constructor_btn()
        assert home_page.get_current_url() == HOME_PAGE_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_feed_btn(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.click_feed_btn()
        assert home_page.get_current_url() == FEED_PAGE_URL

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_modal_open(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.wait_for_element_to_be_clickable(
            home_page_locators.INGREDIENT)
        home_page.click_ingredient()
        assert home_page.is_element_visible(base_page_locators.CONTENT_MODAL)

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_ingredient_modal_close(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.wait_for_element_to_be_clickable(
            home_page_locators.INGREDIENT)
        home_page.click_ingredient()
        home_page.close_modal()
        opened_modals = home_page.find_elements(
            base_page_locators.OPENED_MODAL)
        assert opened_modals == []

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_counter(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.wait_for_element_to_be_clickable(
            home_page_locators.INGREDIENT)
        home_page.drag_and_drop(
            home_page_locators.INGREDIENT, home_page_locators.CONSTRUCTOR_AREA)
        value = home_page.find_element(
            home_page_locators.INGREDIENT_COUNTER).text
        assert value == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_create_order(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.login()
        assert home_page.is_element_visible(home_page_locators.MAKE_ORDER_BTN)

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_profile_page(self, home_page: HomePage):
        home_page.go_to(HOME_PAGE_URL)
        home_page.click_profile_btn()
        assert home_page.get_current_url() == LOGIN_PAGE_URL
