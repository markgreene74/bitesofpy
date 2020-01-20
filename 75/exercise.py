# https://codechalleng.es/bites/75/
wdays = {0: "Su", 1: "Mo", 2: "Tu", 3: "We", 4: "Th", 5: "Fr", 6: "Sa"}


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    result = dict()
    lines = calendar_output.splitlines()

    # example:
    # |    |    |    |    |
    # Su Mo Tu We Th Fr Sa
    #           1  2  3  4

    for line in range(2, len(lines)):
        for i in range(0, 21, 3):
            _ = lines[line][i : i + 2]
            if _ != "  " and _ != "":
                result[int(_)] = wdays[i // 3]
    return result
