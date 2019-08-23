from decimal import Decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    return Decimal(str(number)).quantize(Decimal("1"))