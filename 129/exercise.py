import requests
from collections import defaultdict

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    elif 'M' in cap:
        return float(cap.strip('$').strip('M'))
    elif 'B' in cap:
        return float(cap.strip('$').strip('B')) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    # total = float(0)
    # for i in data:
    #     if i['industry'] == industry:
    #         total += _cap_str_to_mln_float(i['cap'])
    # return round(total, 2)
    return round(sum([_cap_str_to_mln_float(i['cap']) for i in data if i['industry'] == industry]), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    d = defaultdict(float)
    for i in data:
        d[i['symbol']] += _cap_str_to_mln_float(i['cap'])
    return sorted(d.items(), key=lambda x: x[1])[-1][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    d = defaultdict(float)
    for i in data:
        if i['cap'] != 'n/a':
            d[i['sector']] += _cap_str_to_mln_float(i['cap'])
    d_sorted = sorted(d.items(), key=lambda x: x[1])
    return (d_sorted[-1][0], d_sorted[0][0])