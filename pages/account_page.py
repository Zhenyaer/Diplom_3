import allure
from pages.base_page import BasePage
from locators.account_page_locators import LocatorsAccountPage


class AccountPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Личный кабинет"')
    def load_profile_button(self):
        return self.wait_load_element(LocatorsAccountPage.profile_button)

    @allure.step('Клик по кнопке "История заказов')
    def click_on_order_history_button(self):
        return self.click_on_element(LocatorsAccountPage.order_history_button)

    @allure.step('Клик по кнопке "Выход')
    def click_on_logout_button(self):
        return self.click_on_element(LocatorsAccountPage.logout_button)

    @allure.step('Получение списка заказов из истории заказов')
    def get_order_list(self):
        return self.find_elements(LocatorsAccountPage.order_list)
