def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    firstpass = sorted(words, key=lambda x: x.lower())
    return sorted(firstpass, key=lambda x: x[0].isdigit())
