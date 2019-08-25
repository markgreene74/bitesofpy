from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    result = []
    adeck = [
        "0",
        "1",
        "1",
        "2",
        "2",
        "3",
        "3",
        "4",
        "4",
        "5",
        "5",
        "6",
        "6",
        "7",
        "7",
        "8",
        "8",
        "9",
        "9",
        "Draw Two",
        "Draw Two",
        "Skip",
        "Skip",
        "Reverse",
        "Reverse",
    ]
    for asuit in SUITS:
        for acard in adeck:
            result.append(UnoCard(asuit, acard))
    for i in range(4):
        result.append(UnoCard(None, "Wild"))
        result.append(UnoCard(None, "Wild Draw Four"))
    return result
