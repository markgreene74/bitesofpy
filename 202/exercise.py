# https://codechalleng.es/bites/202/
import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / "bites.csv"

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
    output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f.readlines(), delimiter=";")
    d = {}
    for i in reader:
        bite = i["Bite"].split(".")[0].split()[1]
        diff = 0 if i["Difficulty"] == "None" else float(i["Difficulty"])
        d[bite] = diff
    return sorted(d, key=d.get, reverse=True)[:N]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
