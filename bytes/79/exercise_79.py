import csv
import requests
from collections import defaultdict

CSV_URL = "https://bit.ly/2HiD2i8"


def get_csv():
    """Use requests to download the csv and return the
    decoded content"""
    data = requests.get(CSV_URL)
    return csv.DictReader(data.text.splitlines())


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
    and their corresponding member counts in pluses (see Bite/tests)"""
    table = defaultdict(int)
    # content is a csv.DictReader
    for entry in content:
        table[entry["tz"]] += 1
    table_sorted = sorted(table.items(), key=lambda kv: kv[0])
    for i in table_sorted:
        print(f'{i[0].ljust(20)} | {"+" * i[1]}')
