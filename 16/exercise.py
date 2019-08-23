from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    for i in [100, 200, 300, 365, 400, 500, 600, 700, 730, 800]:
        yield PYBITES_BORN + timedelta(days=i)