from collections import OrderedDict, namedtuple

up = 4000

romans = namedtuple("romans", "one, five, nine")
equivalents = {
    "u": romans("I", "V", "IX"),
    "t": romans("X", "L", "XC"),
    "h": romans("C", "D", "CM"),
    "th": romans("M", "V", " "),
}


def translate(num, equivalent):
    one = equivalents[equivalent].one
    five = equivalents[equivalent].five
    nine = equivalents[equivalent].nine
    if num == 0:
        return ""
    elif num < 4:
        return one * num
    elif num == 4:
        return one + five
    elif num == 5:
        return five
    elif num < 9:
        return five + one * (num - 5)
    elif num == 9:
        return nine


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if type(decimal_number) != int or decimal_number not in range(up + 1):
        raise ValueError("There is a problem with the number")
    d = OrderedDict()
    c = 0
    # break the number in units, tens, hundreds, thousands
    while decimal_number != 0:
        d.update({c: decimal_number % 10})
        decimal_number = decimal_number // 10
        c += 1
    # decimal_number = 1246
    # d = OrderedDict([(0, 6), (1, 4), (2, 2), (3, 1)])
    #                   u       t       h       th
    # (th)ousands
    th = translate(d[3], "th") if d.get(3) else ""
    # (h)undreds
    h = translate(d[2], "h") if d.get(2) else ""
    # (t)ens
    t = translate(d[1], "t") if d.get(1) else ""
    # (u)nits
    u = translate(d[0], "u") if d.get(0) else ""
    return th + h + t + u
