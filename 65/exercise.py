import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join("/tmp", "dictionary.txt")
urllib.request.urlretrieve("http://bit.ly/2iQ3dlZ", DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    words_set = set(_get_permutations_draw(draw))
    dictionary_set = set(dictionary)
    return list(words_set & dictionary_set)


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    d_lower = [letter.lower() for letter in draw]
    d_permutations = []
    # [[x for x in itertools.permutations(d_lower, y + 1)] for y in range(len(d_lower))]
    for y in range(len(d_lower)):
        for x in itertools.permutations(d_lower, y + 1):
            d_permutations.append("".join(x))
    return d_permutations
