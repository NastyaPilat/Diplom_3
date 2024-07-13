from selenium.webdriver.common.by import By


CONTENT_MODAL = (By.XPATH, '//*[contains(@class, "Modal_modal__contentBox")]')
ORDER_MODAL = (By.XPATH, '//*[contains(@class, "Modal_orderBox")]')
OPENED_MODAL = (By.XPATH, '//*[contains(@class, "Modal_modal_opened")]')
ORDER_ID_IN_MODAL = (
    By.XPATH, '//*[contains(@class, "Modal_modal_opened")]//h2')
CLOSE_MODAL_BTN = (By.XPATH, '//*[contains(@class, "Modal_modal__close")]')
INPUT = (By.TAG_NAME, 'input')
ORDER_ID = (
    By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits-default")]')
PROFILE_BTN = (By.XPATH, "//a[@href = '/account']")
