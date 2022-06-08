import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import get_locator


class BasePage:
    """
    Класс для базовых операций
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait_five_second = WebDriverWait(self.driver, 7)
        self.search_input = self.driver.find_element(
            By.XPATH, get_locator(locator='search_input'))
        self.button_find = self.driver.find_element(
            By.XPATH, get_locator(locator='find_button'))

    def go_to(self, input_name: str):
        """
        Метод перехода на необходимый ресурс
        :param input_name: название, передаваемое в поисковую строку
        """
        with allure.step(f'Выполнить запрос {input_name}'):
            self.search_input.send_keys(input_name)
            self.wait_element(element=self.button_find)
            self.button_find.click()

    def wait_element(self, element: WebElement):
        """
        Метод ожидания появления элемента
        :param element: веб элемент
        """
        with allure.step('Дождаться элемента'):
            self.wait_five_second.until(EC.element_to_be_clickable(element))

    @staticmethod
    def check_text(expected_value: [str, int], actual_value: [str, int]):
        """
        Метод проверки значения
        :param expected_value: ожидаемое значение
        :param actual_value: фактическое значение
        """
        with allure.step(f'Сравнить значение {actual_value} с '
                         f'ожидаемым {expected_value}'):
            assert expected_value == actual_value,(
                f'Неверное значение: {actual_value}, '
                f'ожидается: {expected_value}')
