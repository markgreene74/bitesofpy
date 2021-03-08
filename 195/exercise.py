# https://codechalleng.es/bites/195/
from collections import namedtuple
import csv
import os
from pathlib import Path
import sqlite3
import random
import string

import requests

DATA_URL = "https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm"
TMP = Path(os.getenv("TMP", "/tmp"))

salt = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = TMP / f"nba_{salt}.db"

Player = namedtuple(
    "Player", ("name year first_year team college active " "games avg_min avg_points")
)

conn = sqlite3.connect(DB)
cur = conn.cursor()


def import_data():
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode("utf-8")

    reader = csv.DictReader(content.splitlines(), delimiter=",")

    players = []
    for row in reader:
        players.append(
            Player(
                name=row["Player"],
                year=row["Draft_Yr"],
                first_year=row["first_year"],
                team=row["Team"],
                college=row["College"],
                active=row["Yrs"],
                games=row["Games"],
                avg_min=row["Minutes.per.Game"],
                avg_points=row["Points.per.Game"],
            )
        )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)"""
    )
    cur.executemany("INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)", players)
    conn.commit()


if DB.stat().st_size == 0:
    print("loading data")
    import_data()


# you code:


def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
    numeric in your SQL query)"""
    _query = cur.execute("SELECT name, avg_points FROM players")
    _dict = {}
    for row in _query:
        _name, _p = row
        _points = float(_p)
        _dict[_points] = _name
    return _dict.get(max(_dict.keys()))


def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    _query = cur.execute('SELECT * FROM players WHERE college == "Duke University"')
    _list = [i for i in _query]
    return len(_list)


def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
    are active ("active" column)"""
    _query = cur.execute(
        'SELECT active FROM players WHERE college == "Stanford University"'
    )
    _list = []
    for row in _query:
        (_years_active,) = row
        _list.append(int(_years_active))
    result = sum(_list) / len(_list)
    return round(result, 2)


def year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    _query = cur.execute("SELECT count(name), year FROM players GROUP BY year")
    _dict = {}
    for row in _query:
        _n_players, _years = row
        _dict[int(_n_players)] = int(_years)
    return _dict.get(max(_dict.keys()))
