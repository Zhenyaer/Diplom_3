from selenium.webdriver.common.by import By


class LocatorsResetPasswordPage:
    SAVE_BUTTON = By.XPATH, './/button[text()="Сохранить"]'  # Кнопка "Сохранить"
    PASSWORD_DIV = By.XPATH, './/div[@class="input__container"]/div'  # Поле "Пароль"
    SHOW_HIDE_PASSWORD_BUTTON = By.XPATH, './/div[@class="input__icon input__icon-action"]'  # Кнопка "Показать/Скрыть пароль"
