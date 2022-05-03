from collections import Counter


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
    an anagram of word1, ignore case and spacing.
    About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    w1 = Counter(word1.lower().replace(" ", ""))
    w2 = Counter(word2.lower().replace(" ", ""))
    return bool(w1 == w2)
