from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    named = namedtuple('named', dict_.keys())
    the_ntuple = named(**dict_)
    return the_ntuple


def nt2json(nt):
    d = nt._asdict()
    d['started'] = d['started'].strftime('%Y-%m-%d %H:%M:%S')
    return json.dumps(d)