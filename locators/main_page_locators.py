from selenium.webdriver.common.by import By


class LocatorsMainPage:
    login_button = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    account_profile_button = By.XPATH, './/a[@href="/account"]'  # Кнопка "Личный кабинет"
    arrange_order_button = By.XPATH, './/button[text()="Оформить заказ"]'  # Кнопка "Оформить заказ"
    order_feed_button = By.XPATH, './/a[@href="/feed"]'  # Кнопка "Лента заказов"
    img_ingredient_R2_D3 = By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]'  # Иконка ингредиента
    section_with_ingredients = By.XPATH, './/div[@class="App_App__aOmNj"]/section'  # Секция ингредиентов
    close_popup_button = By.XPATH, './/section[contains(@class, "Modal_modal_opened")]/div/button'  # Кнопка "Закрыть"
                                                                                                # в секции ингредиентов
    sauce_section = By.XPATH, './/span[text()="Соусы"]'  #Секция соусы
    space_sauce_ingredient = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'  # Иконка фирменного соуса
    crater_bun = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'  # Иконка краторной булочки
    counter_space_sauce_ingredient = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]/div/p'  # Каунтер
                                                                                                     # фирменного соуса
    burger_basket = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'  # Корзина с заказом
    order_status = By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]'  # Статус заказа
    popup_animation_start = By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]'  # Начало анимации окна заказа
    popup_animation_finish = By.XPATH, './/div[@class="Modal_modal__P3_V5"]'  # Конец анимации окна заказа
    order_number_in_popup = By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]'  # Заголовок с номером заказа
