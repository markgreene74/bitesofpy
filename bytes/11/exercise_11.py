# https://codechalleng.es/bites/11/
# https://docs.python.org/3/reference/datamodel.html#special-method-names
class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    # len(acc) returns the number of transactions
    def __len__(self):
        return len(self._transactions)

    # acc1 >,<,>=.<=,== acc2 returns a boolean comparing account balances
    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    # acc[n] shows the nth transaction on account (0 based)
    # list(acc) returns a sequence of account transactions
    def __getitem__(self, position):
        return self._transactions[position]

    # acc + int and acc - int can be used to add/subtract money
    def __add__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("The amount must be an integer")
        self._transactions.append(amount)
        return self.balance

    def __sub__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("The amount must be an integer")
        self._transactions.append(amount * -1)
        return self.balance

    # str(acc) returns NAME account - balance: INT
    def __str__(self):
        return f"{self.name.capitalize()} account - balance: {self.balance}"
