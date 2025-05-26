from selenium.webdriver.common.by import By


class LocatorsForgotPasswordPage:
    email_field = By.XPATH, './/input[@name="name"]' # Поле email
    recovery_button = By.XPATH, './/button[text()="Восстановить"]'  # Кнопка "Войти в аккаунт"
