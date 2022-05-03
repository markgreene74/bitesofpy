from csv import reader
from collections import defaultdict


data = """Luke Skywalker,172,77
          C-3PO,167,75
          R2-D2,96,32
          Darth Vader,202,136
          Leia Organa,150,49
          Owen Lars,178,120
          Beru Whitesun lars,165,75
          R5-D4,97,32
          Biggs Darklighter,183,84
          Obi-Wan Kenobi,182,77
          Anakin Skywalker,188,84
          Chewbacca,228,112
          Han Solo,180,80
          Greedo,173,74
          Jek Tono Porkins,180,110
          Yoda,66,17
          Palpatine,170,75
          Boba Fett,183,78.2
          IG-88,200,140
          Bossk,190,113
"""


def person_max_bmi(data=data):
    """Return (name, BMI float) of the character in data that
    has the highest BMI (rounded on 2 decimals)"""
    characters = defaultdict(float)

    for line in reader(data.splitlines()):
        _bmi = float(line[2]) / ((int(line[1]) / 100) ** 2)
        characters[line[0].strip()] = round(_bmi, 2)

    thewinner = max(characters, key=characters.get)
    return thewinner, characters[thewinner]
