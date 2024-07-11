from selenium.webdriver.common.by import By


OPENED_MODAL = (By.CLASS_NAME, 'Modal_modal_opened__3ISw4')
ORDER_ID_IN_MODAL = (By.XPATH, '//*[@class="Modal_modal_opened__3ISw4"]//h2')
CLOSE_MODAL_BTN = (By.CLASS_NAME, 'Modal_modal__close__TnseK')
INPUT = (By.TAG_NAME, 'input')
ORDER_ID = (
    By.XPATH, '//div[contains(@class, "OrderHistory_textBox__3lgbs")]//p[contains(@class, "text_type_digits-default")]')
PROFILE_BTN = (By.XPATH, "//a[@href = '/account']")
