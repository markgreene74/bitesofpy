# https://codechalleng.es/bites/168/
# https://docs.python.org/3/library/heapq.html
# https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field
from typing import List, Tuple
import heapq


bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """

    name: str
    bites: int

    def __eq__(self, other):
        return self.bites == other.bites

    def __lt__(self, other):
        return self.bites < other.bites

    def __gt__(self, other):
        return self.bites > other.bites

    def __repr__(self):
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    _rankings: List[Ninja] = field(default_factory=list)

    def __post_init__(self):
        heapq.heapify(self._rankings)

    def add(self, n_object):
        return heapq.heappush(self._rankings, n_object)

    def dump(self):
        return heapq.heappop(self._rankings)

    def highest(self, count=1):
        return heapq.nlargest(count, self._rankings, key=lambda x: x.bites)

    def lowest(self, count=1):
        return heapq.nsmallest(count, self._rankings, key=lambda x: x.bites)

    def pair_up(self, count=3):
        _lo = self.lowest(count)
        _hi = self.highest(count)
        return list(zip(_hi, _lo))

    def __len__(self):
        return len(self._rankings)

    def __getitem__(self, position):
        return self._rankings[position]
