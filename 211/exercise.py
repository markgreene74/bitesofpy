# https://codechalleng.es/bites/211/
from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 0
        for attempts in range(MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                print(exc)
        else:
            raise MaxRetriesException("Reached the max number of retries")

    return wrapper
