# https://codechalleng.es/bites/158/
from statistics import median, mean
from decimal import *


class IntList(list):
    def __init__(self, value_list):
        self._validate(value_list)
        super().__init__(value_list)

    def _validate(self, something):
        # make sure that 'something' is either an accepted type or a list of
        # accepted types, raise TypeError if it is not
        accepted_types = (int, float, Decimal)
        if isinstance(something, list) and all(
            isinstance(i, accepted_types) for i in something
        ):
            return True
        elif isinstance(something, accepted_types):
            return True
        else:
            raise TypeError(
                "Expecting a single numerical value or a list of numerical values"
            )

    def append(self, argument):
        self._validate(argument)
        return super().append(argument)

    def __add__(self, argument):
        self._validate(argument)
        return super().__add__(argument)

    def __iadd__(self, argument):
        self._validate(argument)
        return super().__iadd__(argument)

    @property
    def mean(self):
        return mean(int(i) for i in self)

    @property
    def median(self):
        return median(self)
