import allure
from pages.base_page import BasePage
from locators.feed_page_locators import LocatorsFeedPage


class FeedPage(BasePage):

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_on_constractor_button(self):
        return self.click_on_element(LocatorsFeedPage.constractor_button)

    @allure.step('Кликнуть по верхнему заказу')
    def click_on_order(self):
        order = self.get_element(LocatorsFeedPage.upper_order)
        return order.click()

    @allure.step('Получение элемента попапа')
    def get_order_popup(self):
        return self.get_element(LocatorsFeedPage.order_popup)

    @allure.step('Получение количества заказов за все время')
    def get_counter_for_all_time(self):
        counter = self.get_element(LocatorsFeedPage.counter_for_all_time)
        return int(counter.text)

    @allure.step('Получение количества заказов за сегодня')
    def get_counter_for_today(self):
        counter = self.get_element(LocatorsFeedPage.counter_for_today)
        return int(counter.text)

    @allure.step('Получение списка заказов из ленты заказов')
    def get_order_list(self):
        return self.find_elements(LocatorsFeedPage.order_list)

    @allure.step('Получение списка заказов "В работе"')
    def get_order_in_work_list(self):
        return self.find_elements(LocatorsFeedPage.order_in_work_list)

    @allure.step('Ожидание появления списка "В работе"')
    def presence_order_list_in_work_located(self):
        return self.presence_element_located(LocatorsFeedPage.order_in_work_list)

    @allure.step('Ожидание появления заказа в списке "В работе"')
    def presence_order_in_work_list(self, order_number):
        return self.presence_text_in_element(LocatorsFeedPage.order_in_work_list, order_number)
