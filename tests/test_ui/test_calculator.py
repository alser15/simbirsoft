import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.calculator_page import Calculator


@allure.title('Тест на проверку работы калькулятора')
def test_calc(driver: WebDriver, data: dict):
    """
    Тест на проверку работы калькулятора
    :param driver: фикстура подключения к браузеру
    :param data: тест-данные из json файла
    """
    calc = Calculator(driver)
    with allure.step(f'Шаг 1. Открыть браузер и перейти на {data["find"]}'):
        calc.go_to(data['find'])
    with allure.step(f'Шаг 2. Ввести значение {data["expected_value_string"]} '
                     f'{data["expected_value_calc"]}'):
        calc.input_value(calc.button(data['one']),
                         calc.button_action('умножение'),
                         calc.button(data['two']),
                         calc.button_action('вычитание'),
                         calc.button(data['three']),
                         calc.button_action('сложение'),
                         calc.button(data['one']),
                         calc.button_action('равно'))
        with allure.step(f'Шаг 2.1 Проверить значения'):
            calc.get_value(value_calc=calc.input_calc,
                           value_string=calc.memory_string)
            calc.check_text(expected_value=data['expected_value_calc'],
                            actual_value=calc.value_calc)
            calc.check_text(expected_value=data['expected_value_string'],
                            actual_value=calc.value_string)
