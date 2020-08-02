# https://codechalleng.es/bites/291/
from collections import namedtuple
from datetime import timedelta, datetime
from typing import List


def get_time(timestamp_str: str) -> float:
    """This helper function process a timestamp string like
       for example: '00:00:00,000 --> 00:00:01,000'
       and returns the number of seconds as float
    """
    start_str, end_str = timestamp_str.replace("-->", "").split()
    start = datetime.strptime(start_str, "%H:%M:%S,%f")
    end = datetime.strptime(end_str, "%H:%M:%S,%f")

    # for the purpose of the exercise we can just consider seconds
    delta = end.second - start.second
    return float(delta)


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    # create a namedtuple to store each entry (caption) data
    Entry = namedtuple("Entry", ["time", "length", "speed"])

    # create an empty dict, this is where we are going to store
    # the data as namedtuples
    results: dict() = {}

    for entry in text.strip().split("\n\n"):
        # example of the data:
        # lines[0]-> section ("1")
        # lines[1]-> timestamps ("00:00:00,498 --> 00:00:02,827")
        # lines[2]-> caption ("Beautiful is better than ugly.")
        section, timestamps, caption = entry.split("\n")

        section_int = int(section)
        # use a helper function to get the timedelta
        time = get_time(timestamps)
        length = len(caption)

        results[section_int] = Entry(time=time, length=length, speed=(length / time))

    # sort results by speed
    sorted_results = sorted(
        results.keys(), key=lambda x: results[x].speed, reverse=True
    )

    return sorted_results

"""
I am the 9th Pythonista who cracked Bite 291.
Resolution time: ~56 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 53 min. 💪
"""
