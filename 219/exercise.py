# https://codechalleng.es/bites/219/
from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    result_date = start_date
    while True:
        result_date += timedelta(days=num_days)
        for i in range(num_bites):
            yield result_date

'''
Resolution time: ~40 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 15 min. 💪
'''
