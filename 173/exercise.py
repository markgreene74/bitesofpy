# https://codechalleng.es/bites/173/
from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6, hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str, start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    days = int(
        re.search(r"(\d+)d", delay_time).group(1)
        if re.search(r"(\d+)d", delay_time)
        else 0
    )
    hours = int(
        re.search(r"(\d+)h", delay_time).group(1)
        if re.search(r"(\d+)h", delay_time)
        else 0
    )
    minutes = int(
        re.search(r"(\d+)m", delay_time).group(1)
        if re.search(r"(\d+)m", delay_time)
        else 0
    )
    seconds = int(
        re.search(r"(\d+)s", delay_time).group(1)
        if re.search(r"(\d+)s", delay_time)
        else 0
    )
    if delay_time.isdigit():
        seconds += int(delay_time)
    end_time = start_time + timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )
    return f"{task} @ {end_time}"
