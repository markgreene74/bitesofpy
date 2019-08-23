from functools import wraps

def print_text(a_string):
    return a_string

def make_html(element):
    s_open = "<" + element + ">"
    s_close = "</" + element + ">"
    def another_dec(func):
        @wraps(func)
        def wrapper_make_html(*args, **kwargs):
            return f'{s_open}{str(func(*args,**kwargs))}{s_close}'
        return wrapper_make_html
    return another_dec