from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    html = BeautifulSoup(content, 'html.parser')
    find_class = html.find(class_='list-table')

    # build a list with the holiday names
    h_names = [i.text for i in find_class.findAll('a')]

    # build a list with the holiday months
    # this is slightly more complicated
    h_months = []
    for i in find_class.select('td'):
        try:
            something = i.find('time')['datetime']
            if something:
                h_months.append(something.split('-')[1])
        except TypeError:
            pass

    # build tuples with the two lists
    couples = zip(h_months, h_names)
    # build the dictionary
    for k, v in couples:
        holidays[k].append(v)
    return holidays