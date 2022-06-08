import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages import get_locator
from pages.base_page import BasePage


class Calculator(BasePage):
    """
    Класс взаимодействия со страницей калькулятора
    """
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.value_calc = None
        self.value_string = None
        self.button_action = lambda x: self.driver.find_element(
            By.XPATH, get_locator(locator='button_action') % x)
        self.input_calc = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='input_calc'))
        self.button = lambda x: self.driver.find_element(
            By.XPATH, get_locator(locator='button') % x)
        self.memory_string = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='memory_string'))

    def get_value(self, **kwargs):
        """
        Метод установки значения атрибуту класса
        :param kwargs: словарь, где ключ - название атрибута,
        значение - значение атрибута
        """
        for index, key in enumerate(kwargs):
            with allure.step(f'Присвоить атрибуту {key} '
                             f'значение {kwargs[key]().text}'):
                self.__setattr__(key, kwargs[key]().text)

    def input_value(self, *args):
        """
        Метод нажатия на кнопки калькулятора
        :param args: кортеж из значений
        """
        self.wait_element(element=self.input_calc())
        with allure.step(f'Поочередно ввести значения'):
            for obj in args:
                obj.click()
