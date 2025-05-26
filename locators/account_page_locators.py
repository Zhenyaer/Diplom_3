from selenium.webdriver.common.by import By


class LocatorsAccountPage:
    profile_button = By.XPATH, './/a[@href="/account/profile"]'  # Кнопка "Личный кабинет"
    order_history_button = By.XPATH, './/a[@href="/account/order-history"]'  # Кнопка "История заказов"
    logout_button = By.XPATH, './/button[text()="Выход"]'  # Кнопка "Выход"
    order_list = By.XPATH, './/p[@class="text text_type_digits-default"]'  # Список заказов истории заказов
