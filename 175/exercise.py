# https://codechalleng.es/bites/175/

"""
pytest run speed: 1.69 seconds

Disclaimer, I never used Pandas before. I hope real Pandas experts will
forgive any mistake in my approach.

My initial thought was to use set()s, which I am much more familiar with,
but then I looked at the exercise hints and decided to go full Pandas and
this is the result.
"""

from datetime import date
import pandas as pd


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    min_d = min(dates)
    max_d = max(dates)
    dates_idx = pd.DatetimeIndex(dates)
    missing_dates = pd.date_range(start=min_d, end=max_d).difference(dates_idx)
    return pd.to_datetime(missing_dates).date
