# Solved with a oneliner which uses `all()` and `str.isascii()` (Python >= 3.7)


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [i for i in text.split() if not all([j.isascii() for j in i])]
