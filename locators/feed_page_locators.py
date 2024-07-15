from selenium.webdriver.common.by import By


ALL_TIME_ORDERS_COUNTER = (
    By.XPATH, '//div[p[text()="Выполнено за все время:"]]//following-sibling::p[contains(@class, "OrderFeed_number")]')
TODAY_ORDERS_COUNTER = (
    By.XPATH, '//div[p[text()="Выполнено за сегодня:"]]//following-sibling::p[contains(@class, "OrderFeed_number")]')
ORDER_ID_IN_PROGRESS = (
    By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li')
