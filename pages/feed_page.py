import allure
from pages.base_page import BasePage
from locators.feed_page_locators import LocatorsFeedPage
from src.urls import Urls


class FeedPage(BasePage):

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_on_constractor_button(self):
        return self.click_on_element(LocatorsFeedPage.CONSTRACTOR_BUTTON)

    @allure.step('Кликнуть по верхнему заказу')
    def click_on_order(self):
        order = self.get_element(LocatorsFeedPage.UPPER_ORDER)
        return order.click()

    @allure.step('Получение элемента попапа')
    def get_order_popup(self):
        return self.get_element(LocatorsFeedPage.ORDER_POPUP)

    @allure.step('Получение количества заказов за все время')
    def get_counter_for_all_time(self):
        counter = self.get_element(LocatorsFeedPage.COUNTER_FOR_ALL_TIME)
        return int(counter.text)

    @allure.step('Получение количества заказов за сегодня')
    def get_counter_for_today(self):
        counter = self.get_element(LocatorsFeedPage.COUNTER_FOR_TODAY)
        return int(counter.text)

    @allure.step('Получение списка заказов из ленты заказов')
    def get_order_list(self):
        return self.find_elements(LocatorsFeedPage.ORDER_LIST)

    @allure.step('Получение списка заказов "В работе"')
    def get_order_in_work_list(self):
        return self.find_elements(LocatorsFeedPage.ORDER_IN_WORK_LIST)

    @allure.step('Ожидание появления списка "В работе"')
    def presence_order_list_in_work_located(self):
        return self.presence_element_located(LocatorsFeedPage.ORDER_IN_WORK_LIST)

    @allure.step('Ожидание появления заказа в списке "В работе"')
    def presence_order_in_work_list(self, order_number):
        return self.presence_text_in_element(LocatorsFeedPage.ORDER_IN_WORK_LIST, order_number)

    # Проверка, что текущая страница - Главная
    def is_order_feed_page_open(self):
        return self.get_current_url() == Urls.ORDER_FEED_PAGE
