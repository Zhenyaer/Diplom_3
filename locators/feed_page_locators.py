from selenium.webdriver.common.by import By


class LocatorsFeedPage:
    constractor_button = By.XPATH, './/a[@href="/"]'  # Кнопка "Конструктор"
    upper_order = By.XPATH, './/li[contains(@class, "OrderHistory_listItem")][1]'  # Верхний заказ
    order_popup = By.XPATH, './/div[@class="App_App__aOmNj"]/section[2]'  # Секция c попапом заказа
    counter_for_all_time = By.XPATH, './/*[text()="Выполнено за все время:"]/parent::div/p[2]' # Счетчик "Выполнено за все время"
    counter_for_today = By.XPATH, './/*[text()="Выполнено за сегодня:"]/parent::div/p[2]' # Счетчик "Выполнено за сегодня"
    order_list = By.XPATH, './/p[@class="text text_type_digits-default"]'  # Список заказов ленты заказов
    order_in_work_list = By.XPATH, ('.//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]'
                                    '/li[@class="text text_type_digits-default mb-2"]')  # Список заказов "В работе"
