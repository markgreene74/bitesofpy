from collections import Counter
import os
import re
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join("/tmp", "commits")
urlretrieve("https://bit.ly/2H1EuZQ", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"
# re
timestamp_re = re.compile(r"^Date:\s+(.*\s[+-]+\d+)\s|.*")
ins_re = re.compile(r"\s+(\d+)\s+insertions")
del_re = re.compile(r"\s+(\d+)\s+deletions")


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int = None
) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    all_commits = Counter()
    with open(commits) as f:
        data = f.readlines()
    for line in data:
        # all the lines contain a timestamp
        _time = parse(timestamp_re.match(line).group(1))
        _timestamp = YEAR_MONTH.format(y=_time.year, m=_time.month)
        # but not all the lines contain both insertion AND deletion
        _ins = int(ins_re.search(line).group(1)) if ins_re.search(line) else 0
        _del = int(del_re.search(line).group(1)) if del_re.search(line) else 0
        if not year or _time.year == year:
            all_commits[_timestamp] += _ins + _del
        else:
            pass
    #
    result = all_commits.most_common()
    return (result[-1][0], result[0][0])
