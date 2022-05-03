from random import choices


def gen_key(parts=4, chars_per_part=8):
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    newkey = []
    for x in range(parts):
        newkey.append("".join(choices(charset, k=chars_per_part)))
    return "-".join(newkey)
