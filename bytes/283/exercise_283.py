# https://codechalleng.es/bites/283/
import datetime


def tomorrow(someday=None):
    # Your code goes here
    today = someday or datetime.date.today()
    one_day = datetime.timedelta(days=1)
    return today + one_day


"""
Resolution time: ~26 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 9 min. 💪
"""
