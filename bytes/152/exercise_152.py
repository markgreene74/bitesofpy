# https://codechalleng.es/bites/152/
from functools import wraps


DEFAULT_TEXT = (
    "Subscribe to our blog (sidebar) to periodically get "
    "new PyBites Code Challenges (PCCs) in your inbox"
)
DOT = "."


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
    (inclusive) to 'end' (exclusive) = like range.

     So applying this decorator on a function like this and 'text'
     being 'Hello world' it would convert it into 'Hel.. world' when
     applied like this:

     @strip_range(3, 5)
     def gen_output(text):
         return text
    """

    def actual_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # replace characters
            new_str = []
            for i, letter in enumerate(kwargs["text"]):
                if i in range(start, end):
                    new_str.append(DOT)
                else:
                    new_str.append(letter)
            kwargs["text"] = "".join(new_str)
            return f(*args, **kwargs)

        return wrapper

    return actual_decorator
