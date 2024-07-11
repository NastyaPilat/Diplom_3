from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import base_page_locators
import allure


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('go_to')
    def go_to(self, url: str):
        return self.driver.get(url)

    @allure.step('get_current_url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('find_element')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('find_elements')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('click_element')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('execute_script')
    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    @allure.step('wait_for_element_to_be_clickable')
    def wait_for_element_to_be_clickable(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step('wait_for_number_of_windows_to_be')
    def wait_for_number_of_windows_to_be(self, num_windows: int, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(num_windows))

    @allure.step('wait_for_element_to_be_visible')
    def wait_for_element_to_be_visible(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step('switch_to_window')
    def switch_to_window(self, window_index: int):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    @allure.step('drag_and_drop')
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step('close_modal')
    def close_modal(self):
        self.find_element(base_page_locators.CLOSE_MODAL_BTN).click()

    @allure.step('wait_for_url_to_be')
    def wait_for_url_to_be(self, expected_url: str, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
