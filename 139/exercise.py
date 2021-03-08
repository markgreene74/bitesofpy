# https://codechalleng.es/bites/139/
from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates_list = set(re.findall(r"\d{4}-\d{2}-\d{2}", data, re.M))
    return [date.fromisoformat(d) for d in dates_list]


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
    on coding streak.

    Note that a coding streak is defined as consecutive days coded
    since yesterday, because today is not over yet, however if today
    was coded, it counts too of course.

    So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
    the table makes for a 3 days coding streak.

    See the tests for more examples that will be used to pass your code.
    """
    sorted_dates = sorted(dates, reverse=True)
    counter = 0
    for i, d in enumerate(sorted_dates):
        if (TODAY - d).days < 2 + i:
            counter += 1
        else:
            break
    return counter
