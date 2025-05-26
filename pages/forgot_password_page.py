import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import LocatorsForgotPasswordPage


class ForgotPasswordPage(BasePage):

    @allure.step('Заполнить поле Email"')
    def input_email(self, email):
        return self.fill_field(LocatorsForgotPasswordPage.email_field, email)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_on_password_recovery_button(self):
        return self.click_on_element(LocatorsForgotPasswordPage.recovery_button)
