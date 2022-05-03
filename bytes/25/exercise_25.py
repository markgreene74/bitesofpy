import random

BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
bites_done = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:
    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done
        self.all_bites = set(BITES.keys())

    def _pick_random_bite(self):
        self.bites_left = self.all_bites - self.bites_done
        if len(self.bites_left) == 0:
            raise NoBitesAvailable
        else:
            return random.sample(self.bites_left, 1)[0]

    def new_bite(self):
        self.new_pick = self._pick_random_bite()
        self.bites_done.add(self.new_pick)
        return self.new_pick
