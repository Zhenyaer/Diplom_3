import allure
from pages.base_page import BasePage
from locators.main_page_locators import LocatorsMainPage
from src.urls import Urls
from src.data import ControlText


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Логин"')
    def click_on_login_button(self):
        return self.click_on_element(LocatorsMainPage.LOGIN_BUTTON)

    @allure.step('Ожидание загрузки главной страницы')
    def load_arrange_button(self):
        return self.wait_load_element(LocatorsMainPage.ARRANGE_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке "Личный кабинет"')
    def click_on_account_profile_button(self):
        return self.click_on_element(LocatorsMainPage.ACCOUNT_PROFILE_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_on_order_feed_button(self):
        return self.click_on_element(LocatorsMainPage.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        return self.click_on_element(LocatorsMainPage.IMG_INGREDIENT_R2_D3)

    @allure.step('Получение элемента попапа')
    def get_section_with_ingredients(self):
        return self.get_element(LocatorsMainPage.SECTION_WITH_INGREDIENTS)

    @allure.step('Закрыть попап')
    def click_to_close_popup(self):
        return self.click_on_element(LocatorsMainPage.CLOSE_POPUP_BUTTON)

    @allure.step('Переход в секцию "Соусы"')
    def transfer_to_sauce_section(self):
        return self.click_on_element(LocatorsMainPage.SAUCE_SECTION)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        ingredient = self.get_element(LocatorsMainPage.SPACE_SAUCE_INGREDIENT)
        basket = self.get_element(LocatorsMainPage.BURGER_BASKET)
        self.drag_and_drop(ingredient, basket)

    @allure.step('#Добавление булочки в заказ')
    def add_bun_to_order(self):
        bun = self.get_element(LocatorsMainPage.CRATER_BUN)
        basket = self.get_element(LocatorsMainPage.BURGER_BASKET)
        self.drag_and_drop(bun, basket)

    @allure.step('Получение значения счетчика ингредиента')
    def get_counter_ingredients(self):
        counter = self.get_element(LocatorsMainPage.COUNTER_SPACE_SAUCE_INGREDIENT)
        return int(counter.text)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_arrange_order_button(self):
        return self.click_on_element(LocatorsMainPage.ARRANGE_ORDER_BUTTON)

    @allure.step('Получение номера заказа из попапа')
    def get_order_number_from_popup(self):
        return self.find_element(LocatorsMainPage.ORDER_NUMBER_IN_POPUP).text

    @allure.step('Получение статуса заказа')
    def get_order_status(self):
        return self.get_element(LocatorsMainPage.ORDER_STATUS).text

    @allure.step('Создание заказа и получение его номера')
    def create_order_and_return_it_number(self):
        self.add_bun_to_order()
        self.transfer_to_sauce_section()
        self.add_ingredient_to_order()
        self.click_on_arrange_order_button()
        self.presence_element_located(LocatorsMainPage.POPUP_ANIMATION_FINISH)
        order_number = self.get_order_number_from_popup()
        self.click_to_close_popup()
        return order_number

    # Проверка, что текущая страница - Главная
    def is_main_page_open(self):
        return self.get_current_url() == Urls.BASE_URL

    # Проверка статуса заказа
    def is_order_status_is_ready(self):
        return self.get_order_status() == ControlText.ORDER_STATUS_READY
