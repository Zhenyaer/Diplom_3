import allure
from pages.base_page import BasePage
from locators.main_page_locators import LocatorsMainPage


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Логин"')
    def click_on_login_button(self):
        return self.click_on_element(LocatorsMainPage.login_button)

    @allure.step('Ожидание загрузки главной страницы')
    def load_arrange_button(self):
        return self.wait_load_element(LocatorsMainPage.arrange_order_button)

    @allure.step('Кликнуть по кнопке "Личный кабинет"')
    def click_on_account_profile_button(self):
        return self.click_on_element(LocatorsMainPage.account_profile_button)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_on_order_feed_button(self):
        return self.click_on_element(LocatorsMainPage.order_feed_button)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        return self.click_on_element(LocatorsMainPage.img_ingredient_R2_D3)

    @allure.step('Получение элемента попапа')
    def get_section_with_ingredients(self):
        return self.get_element(LocatorsMainPage.section_with_ingredients)

    @allure.step('Закрыть попап')
    def click_to_close_popup(self):
        return self.click_on_element(LocatorsMainPage.close_popup_button)

    @allure.step('Переход в секцию "Соусы"')
    def transfer_to_sauce_section(self):
        return self.click_on_element(LocatorsMainPage.sauce_section)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        ingredient = self.get_element(LocatorsMainPage.space_sauce_ingredient)
        basket = self.get_element(LocatorsMainPage.burger_basket)
        self.drag_and_drop(ingredient, basket)

    @allure.step('#Добавление булочки в заказ')
    def add_bun_to_order(self):
        bun = self.get_element(LocatorsMainPage.crater_bun)
        basket = self.get_element(LocatorsMainPage.burger_basket)
        self.drag_and_drop(bun, basket)

    @allure.step('Получение значения счетчика ингредиента')
    def get_counter_ingredients(self):
        counter = self.get_element(LocatorsMainPage.counter_space_sauce_ingredient)
        return int(counter.text)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_arrange_order_button(self):
        return self.click_on_element(LocatorsMainPage.arrange_order_button)

    @allure.step('Получение номера заказа из попапа')
    def get_order_number_from_popup(self):
        return self.find_element(LocatorsMainPage.order_number_in_popup).text

    @allure.step('Получение статуса заказа')
    def get_order_status(self):
        return self.get_element(LocatorsMainPage.order_status).text

    @allure.step('Создание заказа и получение его номера')
    def create_order_and_return_it_number(self):
        self.add_bun_to_order()
        self.transfer_to_sauce_section()
        self.add_ingredient_to_order()
        self.click_on_arrange_order_button()
        self.presence_element_located(LocatorsMainPage.popup_animation_finish)
        order_number = self.get_order_number_from_popup()
        self.click_to_close_popup()
        return order_number
