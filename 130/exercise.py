from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    listofcars = [x for x in data if x['year'] == year]
    c = Counter([x['automaker'] for x in listofcars])
    car, year = c.most_common()[0]
    return car


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    listofcars = [x for x in data if x['year'] == year]
    c = Counter([x['model'] for x in listofcars if x['automaker'] == automaker])
    return set(c)