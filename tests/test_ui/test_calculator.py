import allure

from pages.calculator_page import Calculator


@allure.title('Тест на проверку работы калькулятора')
def test_calc(driver, data):
    """
    Тест на проверку работы калькулятора
    :param driver: фикстура подключения к браузеру
    :param data: тест-данные из json файла
    """
    calc = Calculator(driver)
    with allure.step(f'Шаг 1. Открыть браузер и перейти на {data["find"]}'):
        calc.go_to(data['find'])
        with allure.step(f'Шаг 1.1 Проверить, что значение '
                         f'калькулятора = {data["expected_value_calc"]}'):
            calc.get_value(calc.input_calc, value_calc=calc.value_calc)
            calc.check_text(expected_value=data['expected_value_calc'],
                            actual_value=calc.value_calc)
    with allure.step(f'Шаг 2. Ввести значение {data["expected_value_string"]} '
                     f'{data["expected_value_calc"]}'):
        calc.input_value(calc.button(data['one']),
                         calc.button_mul(),
                         calc.button(data['two']),
                         calc.button_minus(),
                         calc.button(data['three']),
                         calc.button_plus(),
                         calc.button(data['one']),
                         calc.button_equals())
        with allure.step(f'Проверить значения'):
            calc.get_value(calc.input_calc,
                           calc.memory_string,
                           value_calc=calc.value_calc,
                           value_string=calc.value_string)
            calc.check_text(expected_value=data['expected_value_calc'],
                            actual_value=calc.value_calc)
            calc.check_text(expected_value=data['expected_value_string'],
                            actual_value=calc.value_string)
