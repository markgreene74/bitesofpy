# https://codechalleng.es/bites/220/
from collections import namedtuple, Counter
import re
from typing import NamedTuple
from datetime import timedelta
from math import floor

import feedparser

SPECIAL_GUEST = "Special guest"

# using _ as min/max are builtins
Duration = namedtuple("Duration", "avg max_ min_")

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = "https://bites-data.s3.us-east-2.amazonaws.com/python_bytes"
IGNORE_DOMAINS = {
    "https://pythonbytes.fm",
    "http://pythonbytes.fm",
    "https://twitter.com",
    "https://training.talkpython.fm",
    "https://talkpython.fm",
    "http://testandcode.com",
}


class PythonBytes:
    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(URL).entries

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [ep.itunes_episode for ep in self.entries if domain in ep.summary]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        domain_re = re.compile(r"https?://[^/]+")
        c = Counter()
        for entry in self.entries:
            # we could use a list comprehension instead of the for loop,
            # but it's easier to count domains per episode this way
            _domains = set(domain_re.findall(entry.description)).difference(
                IGNORE_DOMAINS
            )
            c.update(_domains)
        return c.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        special_guest_ep = [
            ep.itunes_episode
            for ep in self.entries
            if "special guest" in ep.description.lower()
        ]
        return len(special_guest_ep)

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        # some intermediate steps
        _all = [en.itunes_duration for en in self.entries if "pythonbytes" in en.link]
        _all_split = [d.split(":") for d in _all]
        _all_timedelta = [
            timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            for h, m, s in _all_split
        ]
        _pairs = [item for item in zip(_all, _all_timedelta)]
        # and finally we can easily get min, max, avg
        _min, _ = min(_pairs, key=lambda x: x[1])
        _max, _ = max(_pairs, key=lambda x: x[1])
        _avg = floor(sum(t_delta.seconds for _, t_delta in _pairs) / len(_pairs))
        return Duration(avg=_avg, max_=_max, min_=_min)