from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, './/a[text()="Восстановить пароль"]'  # Кнопка "Восстановить пароль"
    EMAIL_FIELD = By.XPATH, './/input[@name="name"]'  # Поле email
    PASSWORD_FIELD = By.XPATH, './/input[@name="Пароль"]'  # Поле пароль
    INPUT_BUTTON = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти
