# https://codechalleng.es/bites/235/
from pathlib import Path
from urllib.request import urlretrieve
from collections import namedtuple, defaultdict
import re

tmp = Path("/tmp")
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""

    Test = namedtuple("Test", "n_tests ex_time ratio")
    all_tests = defaultdict(Test)
    match_values = re.compile(
        r"^(?P<bite>\d+)\s.*\s(?P<passed>\d+)\spassed.*\s(?P<seconds>[0-9.]+)\sseconds.*$"
    )

    for line in timings:
        m = match_values.match(line)
        if m:
            _bite_number = m.group("bite")
            _n_tests = int(m.group("passed"))
            _ex_time = float(m.group("seconds"))
            _ratio = _ex_time / _n_tests
            all_tests[_bite_number] = Test(_n_tests, _ex_time, _ratio)

    return sorted(all_tests.keys(), key=lambda x: all_tests[x].ratio)[0]


"""
🥳 You are awesome! You earned the PyBites Black Ninja Belt! 🎉
"""
