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
        self.wait_five_second = WebDriverWait(self.driver, 5)
        self.search_input = self.driver.find_element(
            By.XPATH, get_locator(locator='search_input'))
        self.button_find = self.driver.find_element(
            By.XPATH, get_locator(locator='find_button'))

    def go_to(self, input_name: str):
        with allure.step(f'Выполнить запрос {input_name}'):
            self.search_input.send_keys(input_name)
            self.wait_element(element=self.button_find)
            self.button_find.click()
        return self

    def wait_element(self, element: WebElement):
        with allure.step('Дождаться элемента'):
            self.wait_five_second.until(EC.element_to_be_clickable(element))
        return self

    @staticmethod
    def check_text(expected_value: [str, int], actual_value: [str, int]):
        with allure.step(f'Сравнить значение {actual_value} с '
                         f'ожидаемым {expected_value}'):
            assert expected_value == actual_value,(
                f'Неверное значение: {expected_value}, '
                f'ожидается: {actual_value}')
