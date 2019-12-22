# https://codechalleng.es/bites/197/
from datetime import date
from dateutil.rrule import rrule, MONTHLY, SU


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    # set the 1st of May/year as start date
    start_date = date(year, 5, 1)
    # get a datetime object for the 2nd Sunday of May/year
    _ = rrule(MONTHLY, count=1, byweekday=SU, bysetpos=2, dtstart=start_date)[0]
    # return a date object
    return _.date()
