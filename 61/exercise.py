# https://codechalleng.es/bites/61/
from collections import namedtuple
from itertools import product
import random

ACTIONS = ["draw_card", "play_again", "interchange_cards", "change_turn_direction"]
NUMBERS = range(1, 5)
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

PawCard = namedtuple("PawCard", "card action")


def create_paw_deck(n=8):
    if n in range(1, len(LETTERS) + 1):
        letters = LETTERS[:n]
    else:
        raise ValueError("Unsupported number of letters")

    n_cards = n * len(NUMBERS)
    random_actions = random.sample(range(1, n_cards), n_cards // 4)

    result =[]
    for i, p in enumerate(product(letters, NUMBERS)):
        # 'ABCD ...' x 1234
        # ('A', 1), ('A', 2), ('A', 3), ('A', 4), ('B', 1), ('B', 2) ...
        _card = p[0] + str(p[1])
        _action = random.choice(ACTIONS) if i in random_actions else None
        result.append(PawCard(_card, _action))

    return result
