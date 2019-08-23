def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = 0
    except TypeError:
        raise TypeError('Check the type of numerator, denominator')
    else:
        if result < 0:
            raise ValueError('The result is a negative number')
    return result