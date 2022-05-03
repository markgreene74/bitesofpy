# https://codechalleng.es/bites/126/
import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
    in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return "Not found"


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
    - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
    - return dict with keys=emojis, values=names"""
    d = dict()
    for i in range(START_EMOJI_RANGE, sys.maxunicode + 1):
        try:
            d[chr(i)] = what_means_emoji(chr(i))
        except ValueError:
            pass
    return d


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
    term, print matches to console"""
    term = term.lower()

    emoji_mapping = _make_emoji_mapping()

    # ... your turn ...
    # [k for k,v in d.items() if 'smiling' in v.lower()]
    emoji_list = [k for k, v in emoji_mapping.items() if term in v.lower()]
    for i in emoji_list:
        description = what_means_emoji(i)
        print(f"{description:<60} | {i}")
