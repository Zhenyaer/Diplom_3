import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import LocatorsResetPasswordPage


class ResetPasswordPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Сохранить"')
    def load_save_button(self):
        return self.wait_load_element(LocatorsResetPasswordPage.save_button)

    @allure.step('Кликнуть кнопку "Показать/Скрыть пароль"')
    def click_on_show_hide_password_button(self):
        return self.click_on_element(LocatorsResetPasswordPage.show_hide_password_button)

    @allure.step('Получение элемента поля "Пароль"')
    def get_password_div(self):
        return self.get_element(LocatorsResetPasswordPage.password_div)
