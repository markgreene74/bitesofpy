IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names):
    result = []
    for name in names:
        if len(result) >= 5:
            break
        elif name[0].lower() == IGNORE_CHAR:
            continue
        elif any(letter.isdigit() for letter in name):
            continue
        elif name[0].lower() == QUIT_CHAR:
            break
        else:
            result.append(name)
    return result
