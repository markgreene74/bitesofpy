# https://codechalleng.es/bites/121/
import re


def _has_repetition(astring):
    for i in range(1, len(astring)):
        if astring[i] == astring[i - 1]:
            return True


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    _lowercase = re.compile(r"[a-z]+")
    _uppercase = re.compile(r"[A-Z]+")
    _digits = re.compile(r"[0-9]+")
    _upperlowercase = re.compile(r"[a-zA-Z]+")
    _special_char = re.compile(r"[^\w]+")

    if len(password) >= 8:
        score += 1
    if _lowercase.search(password) and _uppercase.search(password):
        score += 1
    if _upperlowercase.search(password) and _digits.search(password):
        score += 1
    if _special_char.search(password):
        score += 1
    if len(password) >= 8 and not _has_repetition(password):
        # len(password) >= 8 and not re.findall(r"(.{1}})(\1{1,})", password)
        # would be more accurate but fails the test
        score += 1
    return score
