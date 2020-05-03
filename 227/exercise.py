# https://codechalleng.es/bites/227/
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/csv.html#csv.DictWriter
from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError

EXCEPTION = "exception caught"
TMP = Path("/tmp")


def convert_to_csv(json_file):
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501
    csv_file = TMP / json_file.name.replace(".json", ".csv")

    # you code

    # load the file, catch the bad JSON and raise a new JSONDecodeError
    with open(json_file) as f:
        try:
            data = json.load(f)
        except JSONDecodeError as e:
            # print EXCEPTION as requested by the test
            print(EXCEPTION)
            # and then the original exception
            raise JSONDecodeError(e.msg, e.doc, e.pos)

    # data is a dict, but we are looking more specifically
    # for data["mounts"]["collected"]

    # >>> type(data["mounts"]["collected"])
    # <class 'list'>
    collected = data["mounts"]["collected"]
    fieldnames = collected[0].keys()

    # write the portion of data that we are looking for
    # into the csv file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in collected:
            writer.writerow(row)


'''
Resolution time: ~54 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 23 min. 💪
'''
