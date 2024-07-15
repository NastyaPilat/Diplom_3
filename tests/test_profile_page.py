import allure
from endpoints import HISTORY_PAGE_URL, LOGIN_PAGE_URL
from pages.profile_page import ProfilePage
from locators import profile_page_locators


class TestProfilePage():

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_history_page(self, profile_page: ProfilePage):
        profile_page.login()
        profile_page.click_profile_btn()
        profile_page.wait_for_element_to_be_clickable(
            profile_page_locators.HISTORY_BTN)
        profile_page.click_history_btn()
        assert profile_page.get_current_url() == HISTORY_PAGE_URL

    @allure.title('Выход из аккаунта')
    def test_signout(self, profile_page: ProfilePage):
        profile_page.login()
        profile_page.click_profile_btn()
        profile_page.wait_for_element_to_be_clickable(
            profile_page_locators.SIGNOUT_BTN)
        profile_page.click_signout_btn()
        profile_page.wait_for_url_to_be(LOGIN_PAGE_URL)
        assert profile_page.get_current_url() == LOGIN_PAGE_URL
