import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import LocatorsForgotPasswordPage
from src.urls import Urls


class ForgotPasswordPage(BasePage):

    @allure.step('Заполнить поле Email"')
    def input_email(self, email):
        return self.fill_field(LocatorsForgotPasswordPage.EMAIL_FIELD, email)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_on_password_recovery_button(self):
        return self.click_on_element(LocatorsForgotPasswordPage.RECOVERY_BUTTON)

    # Проверка, что текущая страница - "Страница восстановления пароля"
    def is_password_forgot_page_open(self):
        return self.get_current_url() == Urls.PASSWORD_FORGOT_PAGE
