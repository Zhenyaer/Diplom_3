import allure
from src.data import ControlText


class TestMainPage:

    @allure.title('Проверка перехода в ленту заказов')
    def test_transfer_to_order_feed_page(self, driver, main_page, feed_page):
        main_page.click_on_order_feed_button()

        assert feed_page.is_order_feed_page_open()

    @allure.title('Проверка перехода в конструктор')
    def test_transfer_to_constractor(self, driver, main_page, feed_page):
        main_page.click_on_order_feed_button()
        feed_page.click_on_constractor_button()

        assert main_page.is_main_page_open()

    @allure.title('Проверка появления окна с деталями при клике по ингредиенту')
    def test_appear_ingredient_details(self, main_page):
        main_page.click_on_ingredient()
        popup = main_page.get_section_with_ingredients()

        assert ControlText.OPEN_POPUP_CLASS in popup.get_attribute('class')

    @allure.title('Проверка закрытия окна с деталями ингредиента')
    def test_close_ingredient_details(self, main_page):
        main_page.click_on_ingredient()
        main_page.click_to_close_popup()
        close_popup = main_page.get_section_with_ingredients()

        assert ControlText.CLOSE_POPUP_CLASS in close_popup.get_attribute('class')

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении в заказ')
    def test_increase_counter_ingredient_in_order(self, main_page):
        main_page.transfer_to_sauce_section()
        main_page.add_ingredient_to_order()
        main_page.add_ingredient_to_order()
        main_page.add_ingredient_to_order()

        assert main_page.get_counter_ingredients() == 3

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_create_order(self, main_page, user_login):
        main_page.add_bun_to_order()
        main_page.transfer_to_sauce_section()
        main_page.add_ingredient_to_order()
        main_page.add_ingredient_to_order()
        main_page.click_on_arrange_order_button()

        assert main_page.is_order_status_is_ready()
