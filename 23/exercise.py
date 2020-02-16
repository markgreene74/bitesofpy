# https://codechalleng.es/bites/23/
# https://docs.python.org/3/library/difflib.html#sequencematcher-objects
# https://docs.python.org/3/library/itertools.html#itertools.combinations
import os
import re
from difflib import SequenceMatcher
import itertools
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r"<category>([^<]+)</category>")
TEMPFILE = os.path.join("/tmp", "feed")
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/tags.xml", TEMPFILE)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # do your thing ...
    _combinations = [i for i in itertools.combinations(tags, 2)]
    _similar = [
        i
        for i in _combinations
        if SequenceMatcher(lambda x: x == " ", i[0], i[1]).ratio() >= SIMILAR
    ]
    return _similar

'''
Resolution time: ~36 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 32 min. 💪
'''
