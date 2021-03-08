from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
    using TIME_OFFSETS"""
    # check if date is valid
    if not isinstance(date, datetime) or NOW < date:
        raise ValueError("Date is invalid or in the future")

    diff = (NOW - date).total_seconds()

    # if diff is 2 days or more is a special case
    # return the timestamp
    if diff >= 2 * DAY:
        return date.strftime("%m/%d/%y")
    # else find the matching string in TIME_OFFSETS
    else:
        for i in TIME_OFFSETS:
            if diff < i.offset:
                replacement = int(diff / i.divider) if i.divider else int(diff)
                return i.date_str.format(replacement)
                break
