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
        self.calc = lambda :self.driver.find_element(
            By.XPATH, get_locator(locator='calculator'))
        self.input_calc = lambda :self.driver.find_element(
            By.XPATH, get_locator(locator='input_calc'))
        self.button = lambda x:self.driver.find_element(
            By.XPATH, get_locator(locator='button') % x)
        self.button_mul = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='button_mul'))
        self.button_minus = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='button_minus'))
        self.button_plus = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='button_plus'))
        self.button_equals = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='button_equals'))
        self.memory_string = lambda: self.driver.find_element(
            By.XPATH, get_locator(locator='memory_string'))

    def get_value(self, *args, **kwargs):
        self.wait_element(element=self.calc())
        for index, key in enumerate(kwargs):
            with allure.step(f'Присвоить атрибуту {key} '
                             f'значение {args[index]().text}'):
                self.__setattr__(key, args[index]().text)
        return self

    def input_value(self, *args):
        with allure.step(f'Поочередно ввести значения'):
            for obj in args:
                obj.click()
        return self
