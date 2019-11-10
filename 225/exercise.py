PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    # this is one way to solve the exercise:
    # result = []
    # for char in text:
    #     if char.lower() in PYBITES:
    #         result.append(char.lower() if char.isupper() else char.upper())
    #     else:
    #         result.append(char)
    # return ''.join(result)
    #
    # but this feels more pythonic as we are manipulating just strings
    # and also sligthly more clear to read:
    result = ""
    for char in text:
        if char.lower() in PYBITES:
            result += char.lower() if char.isupper() else char.upper()
        else:
            result += char
    return result
