import re


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    try:
        return re.match("^\s+", text).end()
    except AttributeError:
        return 0
