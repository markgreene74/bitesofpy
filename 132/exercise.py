# https://codechalleng.es/bites/132/
VOWELS = list("aeiou")


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    results = dict()
    for word in text.split():
        vowels = [letter for letter in word if letter.lower() in VOWELS]
        results[word.strip()] = len(vowels)
    return max(results.items(), key=lambda x: x[1])
