# https://codechalleng.es/bites/34/
from collections import namedtuple
from datetime import datetime

Transaction = namedtuple("Transaction", "giver points date")
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    def __init__(self, name):
        self.name = name
        self._transactions = []
        self._fans = set()

    @property
    def karma(self):
        return sum(i.points for i in self._transactions)

    @property
    def points(self):
        return [i.points for i in self._transactions]

    @property
    def fans(self):
        return len(self._fans)

    def __add__(self, transaction):
        self._validate(transaction)
        self._transactions.append(transaction)
        self._fans.add(transaction.giver)

    def __str__(self):
        _f = "fans" if self.fans > 1 else "fan"
        return f"{self.name} has a karma of {self.karma} and {self.fans} {_f}"

    def _validate(self, atransaction):
        if not isinstance(atransaction, Transaction):
            raise ValueError
        if atransaction.giver == self.name:
            raise ValueError("cannot increase own karma")
