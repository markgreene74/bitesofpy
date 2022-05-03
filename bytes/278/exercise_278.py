# https://codechalleng.es/bites/278/
from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    c = Counter(numbers)
    major, _ = c.most_common()[0]
    minor, _ = c.most_common()[-1]
    return major, minor


"""
Resolution time: ~22 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 9 min. 💪
"""
