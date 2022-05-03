from collections import OrderedDict
from bisect import bisect_left

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    list_marks = list(HONORS.keys())
    if user_score < MIN_SCORE:
        return None
    elif user_score > MAX_SCORE:
        return belts[-1]
    elif user_score in list_marks:
        place = list_marks.index(user_score)
    else:
        place = bisect_left(list_marks, user_score) - 1
    return HONORS[list_marks[place]]
