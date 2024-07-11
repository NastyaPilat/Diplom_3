from selenium.webdriver.common.by import By


CONSTRUCTOR_BTN = (By.XPATH, '//a[@href="/"]')
FEED_BTN = (By.XPATH, '//a[@href="/feed"]')
INGREDIENT = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
CONSTRUCTOR_AREA = (By.CLASS_NAME, 'BurgerConstructor_basket__29Cd7')
INGREDIENT_COUNTER = (
    By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[@class="counter_counter__num__3nue1"]')
MAKE_ORDER_BTN = (By.XPATH, '//button[text()="Оформить заказ"]')
LOGIN_BTN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")

