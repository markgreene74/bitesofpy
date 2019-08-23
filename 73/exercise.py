import pytz
from datetime import datetime, timezone

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    all_tzs = [utc.astimezone(pytz.utc).hour]
    for i in timezones:
        # check if i is a valid timezone
        if i not in TIMEZONES:
            raise ValueError
        # else
        all_tzs.append(utc.astimezone(pytz.timezone(i)).hour)
    return all(h in MEETING_HOURS for h in all_tzs)
