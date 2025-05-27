from selenium.webdriver.common.by import By


class LocatorsMainPage:
    LOGIN_BUTTON = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    ACCOUNT_PROFILE_BUTTON = By.XPATH, './/a[@href="/account"]'  # Кнопка "Личный кабинет"
    ARRANGE_ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'  # Кнопка "Оформить заказ"
    ORDER_FEED_BUTTON = By.XPATH, './/a[@href="/feed"]'  # Кнопка "Лента заказов"
    IMG_INGREDIENT_R2_D3 = By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]'  # Иконка ингредиента
    SECTION_WITH_INGREDIENTS = By.XPATH, './/div[@class="App_App__aOmNj"]/section'  # Секция ингредиентов
    CLOSE_POPUP_BUTTON = By.XPATH, './/section[contains(@class, "Modal_modal_opened")]/div/button'  # Кнопка "Закрыть"
                                                                                                # в секции ингредиентов
    SAUCE_SECTION = By.XPATH, './/span[text()="Соусы"]'  #Секция соусы
    SPACE_SAUCE_INGREDIENT = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'  # Иконка фирменного соуса
    CRATER_BUN = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'  # Иконка краторной булочки
    COUNTER_SPACE_SAUCE_INGREDIENT = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]/div/p'  # Каунтер
                                                                                                     # фирменного соуса
    BURGER_BASKET = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'  # Корзина с заказом
    ORDER_STATUS = By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]'  # Статус заказа
    POPUP_ANIMATION_START = By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]'  # Начало анимации окна заказа
    POPUP_ANIMATION_FINISH = By.XPATH, './/div[@class="Modal_modal__P3_V5"]'  # Конец анимации окна заказа
    ORDER_NUMBER_IN_POPUP = By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]'  # Заголовок с номером заказа
