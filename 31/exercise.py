# https://codechalleng.es/bites/31/
# https://www.python.org/dev/peps/pep-0465/
from itertools import chain


class Matrix(object):
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def _mult_lists(self, list_a, list_b):
        result = []
        for i in [0, len(self.values)]:
            result.append(
                [
                    list_a[0 + i] * list_b[0] + list_a[1 + i] * list_b[2],
                    list_a[0 + i] * list_b[1] + list_a[1 + i] * list_b[3],
                ]
            )
        return result

    def __matmul__(self, other):
        # flat list of all the elements in Matrix A (self)
        flat_a = list(chain.from_iterable(self.values))
        # flat list of all the elements in Matrix B (other)
        flat_b = list(chain.from_iterable(other.values))
        return Matrix(self._mult_lists(flat_a, flat_b))

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __imatmul__(self, other):
        self.values = self.__matmul__(other).values
        return self
