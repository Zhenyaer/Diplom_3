import requests
import pytest
from src.data import create_user_data
from src.urls import Urls
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.account_page import AccountPage
from pages.feed_page import FeedPage


# Создание пользователя с его последующим удалением
@pytest.fixture()
def user_create_with_delete():
    user_data = create_user_data()
    response = requests.post(Urls.user_create, json=user_data)
    access_token = response.json()['accessToken']
    yield user_data
    header = {'Authorization': access_token}
    requests.delete(Urls.user_delete, headers=header)


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.base_url)
        yield driver
        driver.quit()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Urls.base_url)
        yield driver
        driver.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture()
def reset_password_page(driver):
    return ResetPasswordPage(driver)


# Авторизация пользователя
@pytest.fixture()
def user_login(user_create_with_delete, login_page):
    email = user_create_with_delete['email']
    password = user_create_with_delete['password']
    login_page.authorization_user(email, password)


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def feed_page(driver):
    return FeedPage(driver)
