from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    password_recovery_button = By.XPATH, './/a[text()="Восстановить пароль"]'  # Кнопка "Восстановить пароль"
    email_field = By.XPATH, './/input[@name="name"]'  # Поле email
    password_field = By.XPATH, './/input[@name="Пароль"]'  # Поле пароль
    input_button = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти
