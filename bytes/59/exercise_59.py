class MultiplicationTable:
    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
        their calculations (form of caching)"""
        self.length = length
        self._table = []
        for x in range(1, self.length + 1):
            self._table.append([x * y for y in range(1, self.length + 1)])
        print(self._table)

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.length ** 2

    def __str__(self):
        """Returns a string representation of the table"""
        result = ""
        for x in self._table:
            result += " | ".join([str(y) for y in x]) + "\n"
        return result

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        if x in range(1, self.length + 1) and y in range(1, self.length + 1):
            return self._table[x - 1][y - 1]
        else:
            raise IndexError
