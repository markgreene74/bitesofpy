import os
import urllib.request
import re

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    with open(LOG) as f:
        data_read = f.read()
    # build a list of all the matches for 'sending to slack channel'
    # and grab the relevant part of the string (date, title)
    match_sent = re.compile(r'''^(\d+\-\d+\s\d+\:\d+.*)\n
                                .*\ssending\sto
                                \sslack\schannel''', re.VERBOSE|re.MULTILINE)
    match_list = match_sent.findall(data_read)
    # build the result dictionary
    result = {}
    for item in match_list:
        toprint = PY_BOOK if 'python' in item.lower() else OTHER_BOOK
        try:
            result[item.split()[0]] += toprint
        except KeyError:
            result[item.split()[0]] = toprint
    # print the results in a fancy way
    for key in result.keys():
        print(f'{key} {result[key]}')