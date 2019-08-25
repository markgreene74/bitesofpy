from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join("/tmp", "course_timings")
urllib.request.urlretrieve("http://bit.ly/2Eb0iQF", COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as f:
        data = f.read()
    return re.findall(r"\((\d+:\d+)\)", data)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    result = timedelta(minutes=0, seconds=0)
    for item in timestamps:
        m, s = item.split(":")
        td = timedelta(minutes=int(m), seconds=int(s))
        result += td
    return str(result)
