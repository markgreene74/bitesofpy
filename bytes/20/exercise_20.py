# https://codechalleng.es/bites/20/
class Account:
    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        # copy the initial state
        self.initial = self._transactions.copy()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.balance < 0:
            # rollback to the initial state
            self._transactions = self.initial
