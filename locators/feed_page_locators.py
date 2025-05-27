from selenium.webdriver.common.by import By


class LocatorsFeedPage:
    CONSTRACTOR_BUTTON = By.XPATH, './/a[@href="/"]'  # Кнопка "Конструктор"
    UPPER_ORDER = By.XPATH, './/li[contains(@class, "OrderHistory_listItem")][1]'  # Верхний заказ
    ORDER_POPUP = By.XPATH, './/div[@class="App_App__aOmNj"]/section[2]'  # Секция c попапом заказа
    COUNTER_FOR_ALL_TIME = By.XPATH, './/*[text()="Выполнено за все время:"]/parent::div/p[2]' # Счетчик "Выполнено за все время"
    COUNTER_FOR_TODAY = By.XPATH, './/*[text()="Выполнено за сегодня:"]/parent::div/p[2]' # Счетчик "Выполнено за сегодня"
    ORDER_LIST = By.XPATH, './/p[@class="text text_type_digits-default"]'  # Список заказов ленты заказов
    ORDER_IN_WORK_LIST = By.XPATH, ('.//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]'
                                    '/li[@class="text text_type_digits-default mb-2"]')  # Список заказов "В работе"
