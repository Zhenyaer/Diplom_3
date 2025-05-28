from selenium.webdriver.common.by import By


class LocatorsForgotPasswordPage:
    EMAIL_FIELD = By.XPATH, './/input[@name="name"]'  # Поле email
    RECOVERY_BUTTON = By.XPATH, './/button[text()="Восстановить"]'  # Кнопка "Войти в аккаунт"
