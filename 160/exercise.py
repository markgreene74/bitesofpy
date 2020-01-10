# https://codechalleng.es/bites/160/
import csv
import os
from urllib.request import urlretrieve
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = "battle-table.csv"
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    with open(BATTLE_DATA) as f:
        reader = csv.DictReader(f.readlines())

    mapping_dict = defaultdict(dict)

    for row in reader:
        _inner_d = defaultdict(list)
        for k in row.keys():
            if row[k] == "win":
                _inner_d["win"].append(k)
            elif row[k] == "lose":
                _inner_d["lose"].append(k)
        mapping_dict[row["Attacker"]] = _inner_d
    return mapping_dict


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()

    if not (player1 in defeat_mapping and player2 in defeat_mapping):
        raise ValueError("Invalid player string(s)")

    if player1 == player2:
        return "Tie"
    elif player2 in defeat_mapping[player1]["win"]:
        return player1  # Player1 win
    elif player2 in defeat_mapping[player1]["lose"]:
        return player2  # Player2 win
