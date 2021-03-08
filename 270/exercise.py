# https://codechalleng.es/bites/270/
from collections import Counter


def freq_digit(num: int) -> int:
    c = Counter(str(num))
    n, freq = c.most_common(1)[0]
    return int(n)


"""
Resolution time: ~30 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 7 min. 💪
"""
