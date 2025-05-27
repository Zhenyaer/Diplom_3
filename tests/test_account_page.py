import allure


class TestAccountPage:

    @allure.title('Проверка перехода в личный кабинет')
    def test_transfer_to_account(self, driver, user_login, main_page, account_page):
        main_page.load_arrange_button()
        main_page.click_on_account_profile_button()
        account_page.load_profile_button()

        assert account_page.is_account_profile_page_open()

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_transfer_to_order_history(self, driver, user_login, main_page, account_page):
        main_page.load_arrange_button()
        main_page.click_on_account_profile_button()
        account_page.load_profile_button()
        account_page.click_on_order_history_button()

        assert account_page.is_order_history_page_open()

    @allure.title('Проверка выхода из аккаунта в разделe "История заказов"')
    def test_logout_from_account_page(self, driver, user_login, main_page, account_page, login_page):
        main_page.load_arrange_button()
        main_page.click_on_account_profile_button()
        account_page.load_profile_button()
        account_page.click_on_logout_button()
        login_page.load_input_button()

        assert login_page.is_login_page_open()
