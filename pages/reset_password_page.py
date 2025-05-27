import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import LocatorsResetPasswordPage
from src.urls import Urls


class ResetPasswordPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Сохранить"')
    def load_save_button(self):
        return self.wait_load_element(LocatorsResetPasswordPage.SAVE_BUTTON)

    @allure.step('Кликнуть кнопку "Показать/Скрыть пароль"')
    def click_on_show_hide_password_button(self):
        return self.click_on_element(LocatorsResetPasswordPage.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('Получение элемента поля "Пароль"')
    def get_password_div(self):
        return self.get_element(LocatorsResetPasswordPage.PASSWORD_DIV)

    # Проверка, что текущая страница - "Страница смены пароля"
    def is_password_reset_page_open(self):
        return self.get_current_url() == Urls.PASSWORD_RESET_PAGE
