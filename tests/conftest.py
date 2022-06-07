import json
from pathlib import Path

import allure
from selenium.webdriver.chrome.service import Service
import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from config import GOOGLE_CONF


@allure.title('Передача веб-драйвера')
@pytest.fixture
def driver() -> WebDriver:
    """
    Фикстура открытия браузера (если нет webdriver, устанавливает его)
    :yyield WebDriver: временная передача драйвера
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(GOOGLE_CONF.url)

    yield driver

    driver.close()


@allure.title('Тест данные')
@pytest.fixture
def data(request: SubRequest) -> dict:
    """
    Фикстура передачи тест данных
    :param request: объект request для анализа контекста запрашивающей
    тестовой функции, класса или модуля
    :return dict: dict
    """
    name_test = request.node.name

    path = "\\".join(request.fspath.strpath.split('\\')[-2:])

    path_file = (str(
        Path(__file__).parent.parent
    ) + '\\' + r'resource' + '\\' + path).replace('py', 'json')

    with open(path_file, 'r', encoding="UTF-8") as file:
        return json.loads(file.read())[name_test]
