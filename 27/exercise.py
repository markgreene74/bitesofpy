import collections
import glob
import json
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    result = []
    for file in files:
        with open(file) as f:
            result.append(json.loads(f.read()))
    return result


def get_single_comedy(movies):
    _alist = [movie['Title'] for movie in movies if 'Comedy' in movie['Genre']]
    return ''.join(_alist)


def get_movie_most_nominations(movies):
    _adict = {}
    for movie in movies:
        numbers = re.findall(r'\&\s(\d+)\s\w+\.', movie['Awards'])[0]
        _adict[movie['Title']] = int(numbers)
    c = collections.Counter(_adict)
    return c.most_common(1)[0][0]


def get_movie_longest_runtime(movies):
    _adict = {}
    for movie in movies:
        numbers = re.findall(r'(\d+)\s\w+', movie['Runtime'])[0]
        _adict[movie['Title']] = int(numbers)
    c = collections.Counter(_adict)
    return c.most_common(1)[0][0]