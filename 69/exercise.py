import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    expr = re.compile(r"\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}")
    return bool(expr.search(text))


def is_integer(number):
    """Return True if number is an integer"""
    return True if type(number) == int else False


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    expr = re.compile(r".*\w+\-\w+.*")
    return bool(expr.search(text))


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    expr = re.compile(r"(\s*\([^()]*\)*)")
    return expr.sub("", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    expr = re.compile(r"\s*[?!.,;]+\s*")
    return [i for i in expr.split(text) if i]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    expr = re.compile(r"\s\s+")
    return expr.sub(" ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    expr = re.compile(r"[aeiouAEIOU]{3}")
    return bool(expr.search(word))


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    expr = re.compile(r"(\d+\/)(\d+\/)(\d+)")
    return expr.sub(r"\2\1\3", date)
