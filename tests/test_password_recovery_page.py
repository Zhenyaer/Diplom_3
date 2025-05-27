import allure
from src.data import create_user_data
from src.data import ControlText


class TestsPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_open_password_recovery_page(self, driver, main_page, login_page, forgot_password_page):
        main_page.click_on_login_button()
        login_page.click_on_password_recovery_button()

        assert forgot_password_page.is_password_forgot_page_open()

    @allure.title('Проверка перехода на страницу смены пароля')
    def test_open_password_reset_page(self, driver, main_page, login_page, forgot_password_page, reset_password_page):
        main_page.click_on_login_button()
        login_page.click_on_password_recovery_button()
        email = create_user_data()['email']
        forgot_password_page.input_email(email)
        forgot_password_page.click_on_password_recovery_button()
        reset_password_page.load_save_button()

        assert reset_password_page.is_password_reset_page_open()

    @allure.title('Проверка активации поля "Пароль" по клику по кнопке "Показать/скрыть пароль"')
    def test_activation_password_field_with_click_on_hidden_button(self, main_page, login_page,
                                                                   forgot_password_page, reset_password_page):
        main_page.click_on_login_button()
        login_page.click_on_password_recovery_button()
        email = create_user_data()['email']
        forgot_password_page.input_email(email)
        forgot_password_page.click_on_password_recovery_button()
        reset_password_page.load_save_button()
        reset_password_page.click_on_show_hide_password_button()
        actual_element = reset_password_page.get_password_div()

        assert ControlText.STATUS_PASSWORD_FIELD_CLASS in actual_element.get_attribute('class')
