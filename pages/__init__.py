import inspect
from pathlib import Path

import yaml


def get_locator(locator: str) -> str:
    """
    Функция получения переменных из файла any_page.yaml
    :param locator: название переменной
    :return str: str
    """
    file = inspect.getouterframes(
        inspect.currentframe())[1].filename.split('\\')[-1][:-3]
    with open(f"{Path(__file__).parent.parent}\\resource\\page_yaml\\"
              f"{file}.yaml", encoding="UTF-8") as name_locator:
        return yaml.safe_load(name_locator)[locator]
