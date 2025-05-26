import allure
from pages.base_page import BasePage
from locators.login_page_locators import LocatorsLoginPage
from src.urls import Urls


class LoginPage(BasePage):

    @allure.step('Кликнуть по кнопке "Восстановить пароль"')
    def click_on_password_recovery_button(self):
        return self.click_on_element(LocatorsLoginPage.password_recovery_button)

    @allure.step('Заполнить поле "Email"')
    def input_email(self, email):
        return self.fill_field(LocatorsLoginPage.email_field, email)

    @allure.step('Заполнить поле "Пароль"')
    def input_password(self, password):
        return self.fill_field(LocatorsLoginPage.password_field, password)

    @allure.step('Кликнуть кнопку "Войти"')
    def click_input_button(self):
        return self.click_on_element(LocatorsLoginPage.input_button)

    @allure.step('Авторизация пользователя')
    def authorization_user(self, email, password):
        self.open_url(Urls.url_login_page)
        self.input_email(email)
        self.input_password(password)
        self.click_input_button()

    @allure.step('Ожидание загрузки страницы')
    def load_input_button(self):
        return self.wait_load_element(LocatorsLoginPage.input_button)
