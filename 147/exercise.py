# https://codechalleng.es/bites/147/
from datetime import date

from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    # use a 'for' loop instead of list comprehension
    # to improve readability
    result = []
    for i in range(0, 100):
        _d = rrule(DAILY, byweekday=(MO, TU, WE, TH, FR), dtstart=start_date)[i]
        result.append(_d.date())
    return result
