from selenium.webdriver.common.by import By


class LocatorsResetPasswordPage:
    save_button = By.XPATH, './/button[text()="Сохранить"]'  # Кнопка "Сохранить"
    password_div = By.XPATH, './/div[@class="input__container"]/div'  # Поле "Пароль"
    show_hide_password_button = By.XPATH, './/div[@class="input__icon input__icon-action"]'  # Кнопка "Показать/Скрыть пароль"
