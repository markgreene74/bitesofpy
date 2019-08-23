from datetime import datetime
from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    if naive_utc_dt.tzinfo == None:
        # check if it's naive
        return (naive_utc_dt.astimezone(AUSTRALIA), naive_utc_dt.astimezone(SPAIN))