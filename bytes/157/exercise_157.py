# https://codechalleng.es/bites/157/
# https://docs.python.org/3/howto/unicode.html#comparing-strings
import unicodedata


def filter_accents(text):
    """Return a sequence of accented characters found in
    the passed in lowercased text string
    """
    return sorted(set(i.lower() for i in text if "WITH" in unicodedata.name(i)))
