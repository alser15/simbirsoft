import inspect
from pathlib import Path

import yaml


def get_locator(locator: str):
    """
    Функция получения переменных из фалйа env.yaml
    :param name_env: название переменной
    :return:
    """
    file = inspect.getouterframes(
        inspect.currentframe())[1].filename.split('\\')[-1][:-3]
    with open(f"{Path(__file__).parent.parent}\\resource\\page_yaml\\"
              f"{file}.yaml") as name_locator:
        return yaml.safe_load(name_locator)[locator]
