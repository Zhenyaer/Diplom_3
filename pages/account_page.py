import allure
from pages.base_page import BasePage
from locators.account_page_locators import LocatorsAccountPage
from src.urls import Urls


class AccountPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Личный кабинет"')
    def load_profile_button(self):
        return self.wait_load_element(LocatorsAccountPage.PROFILE_BUTTON)

    @allure.step('Клик по кнопке "История заказов')
    def click_on_order_history_button(self):
        return self.click_on_element(LocatorsAccountPage.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход')
    def click_on_logout_button(self):
        return self.click_on_element(LocatorsAccountPage.LOGOUT_BUTTON)

    @allure.step('Получение списка заказов из истории заказов')
    def get_order_list(self):
        return self.find_elements(LocatorsAccountPage.ORDER_LIST)

    # Проверка, что текущая страница - "Личный кабинет""
    def is_account_profile_page_open(self):
        return self.get_current_url() == Urls.ACCOUNT_PROFILE_PAGE

    # Проверка, что текущая страница - "История заказов"
    def is_order_history_page_open(self):
        return self.get_current_url() == Urls.ACCOUNT_ORDER_HISTORY_PAGE
