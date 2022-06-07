from pathlib import Path

import yaml

from config.google import Google


def get(name_env: str):
    """
    Функция получения переменных из фалйа env.yaml
    :param name_env: название переменной
    :return:
    """
    with open(f"{Path(__file__).parent.parent}\\env.yaml") as file:
        return yaml.safe_load(file)[name_env]


GOOGLE_CONF = Google(
    url=get(name_env='GOOGLE')
)
