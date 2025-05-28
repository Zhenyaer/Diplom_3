import allure
from src.data import ControlText


class TestFeedPage:

    @allure.title('Проверка открытия окна с деталями заказа')
    def test_open_order_details(self, main_page, feed_page):
        main_page.click_on_order_feed_button()
        feed_page.click_on_order()
        popup = feed_page.get_order_popup()

        assert ControlText.CLOSE_POPUP_CLASS in popup.get_attribute('class')

    @allure.title('Проверка наличия заказа пользователя в истории заказов')
    def test_exist_user_order_in_order_history(self, user_login, main_page, feed_page, account_page):
        order_number = main_page.create_order_and_return_it_number()
        main_page.click_on_account_profile_button()
        account_page.load_profile_button()
        account_page.click_on_order_history_button()

        assert order_number in account_page.get_order_list().text

    @allure.title('Проверка наличия заказа пользователя в ленте заказов')
    def test_exist_user_order_on_feed(self, user_login, main_page, feed_page, account_page):
        order_number = main_page.create_order_and_return_it_number()
        main_page.click_on_order_feed_button()

        assert order_number in feed_page.get_order_list().text

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" после оформления заказа')
    def test_increase_counter_for_all_time(self, user_login, main_page, feed_page):
        main_page.click_on_order_feed_button()
        start_counter = feed_page.get_counter_for_all_time()
        feed_page.click_on_constractor_button()
        main_page.create_order_and_return_it_number()
        main_page.click_on_order_feed_button()
        finish_counter = feed_page.get_counter_for_all_time()

        assert finish_counter > start_counter

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" после оформления заказа')
    def test_increase_counter_for_today(self, user_login, main_page, feed_page):
        main_page.click_on_order_feed_button()
        start_counter = feed_page.get_counter_for_today()
        feed_page.click_on_constractor_button()
        main_page.create_order_and_return_it_number()
        main_page.click_on_order_feed_button()
        finish_counter = feed_page.get_counter_for_today()

        assert finish_counter > start_counter

    @allure.title('Проверка появления оформленного заказа в разделе "В работе"')
    def test_add_order_in_work_list(self, user_login, main_page, feed_page):
        order_number = main_page.create_order_and_return_it_number()
        main_page.click_on_order_feed_button()
        feed_page.presence_order_list_in_work_located()
        feed_page.presence_order_in_work_list(order_number)

        assert order_number in feed_page.get_order_in_work_list().text
