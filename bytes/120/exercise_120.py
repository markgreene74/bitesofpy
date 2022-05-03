from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def wrapper(*args):
        if all(isinstance(i, int) for i in args):
            if all(i > 0 for i in args):
                return func(*args)
            else:
                raise ValueError("All arguments must be greater than zero")
        else:
            raise TypeError("All arguments must be integers")

    return wrapper
