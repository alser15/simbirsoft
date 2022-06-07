import dataclasses
from typing import Callable


@dataclasses.dataclass
class Google:
    url: Callable
