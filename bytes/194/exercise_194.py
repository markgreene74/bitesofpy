# https://codechalleng.es/bites/194/
# https://docs.python.org/3/library/functools.html#functools.lru_cache
from functools import lru_cache


@lru_cache(maxsize=None)
def cached_fib(n):
    if n < 2:
        return n
    return cached_fib(n - 1) + cached_fib(n - 2)


"""
Resolution time: ~25 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 10 min. 💪
"""
