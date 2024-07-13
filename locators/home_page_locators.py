from selenium.webdriver.common.by import By


CONSTRUCTOR_BTN = (By.XPATH, '//a[@href="/"]')
FEED_BTN = (By.XPATH, '//a[@href="/feed"]')
INGREDIENT = (
    By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa6d")]')
CONSTRUCTOR_AREA = (
    By.XPATH, '//*[contains(@class, "BurgerConstructor_basket")]')
INGREDIENT_COUNTER = (
    By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa6d")]//p[contains(@class, "counter_counter__num")]')
MAKE_ORDER_BTN = (By.XPATH, '//button[text()="Оформить заказ"]')
LOGIN_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
