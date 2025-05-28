from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Поиск элемента
    def find_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Поиск нескольких элементов
    def find_elements(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Кликнуть по элементу
    def click_on_element(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.find_element(locator).click()

    # Заполнение поля
    def fill_field(self, locator, text):
        return self.find_element(locator).send_keys(text)

    # Ожидание загрузки элемента
    def wait_load_element(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    # Проверка наличия элемента
    def get_element(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until((expected_conditions.visibility_of_element_located(locator)))

    # Открыть страницу
    def open_url(self, url):
        return self.driver.get(url)

    # Перенос элемента
    def drag_and_drop(self, element, target):
        return drag_and_drop(self.driver, element, target)

    # Ожидание появления элемента
    def presence_element_located(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    # Проверка появления текста к элементе
    def presence_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.text_to_be_present_in_element(locator, text))

    # Получение текущего url
    def get_current_url(self):
        return self.driver.current_url
