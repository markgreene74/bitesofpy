# https://codechalleng.es/bites/230/

# https://docs.python.org/3/reference/datamodel.html#special-method-names
# https://github.com/markgreene74/bitesofpy/blob/master/31/exercise.py

THUMBS_UP, THUMBS_DOWN = "👍", "👎"


class Thumbs:
    # def __init__(self):
    #     pass

    def __mul__(self, other):
        if other == 0:
            raise ValueError("Specify a number")

        thumb = THUMBS_UP if other > 0 else THUMBS_DOWN
        n_thumbs = abs(other)

        if n_thumbs > 3:
            return f"{thumb} ({str(n_thumbs)}x)"
        else:
            return f"{thumb * n_thumbs}"

    def __rmul__(self, other):
        return self.__mul__(other)


"""
Resolution time: ~40 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 21 min. 💪
"""
