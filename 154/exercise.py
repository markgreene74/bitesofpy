# https://codechalleng.es/bites/154/
# https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
# https://www.python.org/dev/peps/pep-0557/
from dataclasses import dataclass


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        self.title = self.title.capitalize()
