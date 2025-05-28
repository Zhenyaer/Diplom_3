from selenium.webdriver.common.by import By


class LocatorsAccountPage:
    PROFILE_BUTTON = By.XPATH, './/a[@href="/account/profile"]'  # Кнопка "Личный кабинет"
    ORDER_HISTORY_BUTTON = By.XPATH, './/a[@href="/account/order-history"]'  # Кнопка "История заказов"
    LOGOUT_BUTTON = By.XPATH, './/button[text()="Выход"]'  # Кнопка "Выход"
    ORDER_LIST = By.XPATH, './/p[@class="text text_type_digits-default"]'  # Список заказов истории заказов
