def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if fmt.lower() == "in":
        original_fmt = "cm"
        factor = 1 / 2.54
    elif fmt.lower() == "cm":
        original_fmt = "in"
        factor = 2.54
    else:
        raise ValueError

    if type(value) == int or type(value) == float:
        return round(value * factor, 4)
    else:
        raise TypeError
