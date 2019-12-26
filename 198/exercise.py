# https://codechalleng.es/bites/198/
from datetime import datetime, timedelta
from dateutil.parser import parse


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    # use parse to get all the dates
    dates = [
        parse(line.split("~")[1].strip())
        for line in reboots.splitlines()
        if "~" in line
    ]
    # this dict contains all the pairs {uptime: datetime}
    d = {}
    # sort the dates so that we start from the earliest timestamp
    s_dates = sorted(dates)
    for i, adate in enumerate(s_dates):
        if i == 0:
            # uptime has to be a timedelta object!
            # in case of the first date in the list we
            # assume uptime will be 0
            uptime = timedelta(0)
        else:
            # uptime is a timedelta of (date - previous date)
            uptime = adate - s_dates[i - 1]
        d[uptime] = adate
    # find the entry with the greatest uptime and build the elements
    # of the tuple that we are going to return
    max_uptime = max(d.keys())
    timestamp = d[max_uptime].strftime("%Y-%m-%d")
    return max_uptime.days, timestamp
