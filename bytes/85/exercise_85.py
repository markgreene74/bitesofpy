# https://codechalleng.es/bites/85/
# https://docs.python.org/3.8/howto/descriptor.html#properties
scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = "white yellow orange green blue brown black paneled red".split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:
    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        # find the tier corresponding to new_score
        belt_score = max([i for i in scores if i <= new_score], default=0)
        # get the corresponding belt
        return BELTS.get(belt_score)

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        # new_score NOT an int or new_score less than current score
        if not (isinstance(new_score, int) and new_score > self._score):
            raise ValueError
        belt = self._get_belt(new_score)
        if belt != self._last_earned_belt:
            self._last_earned_belt = belt
            message = (
                f"Congrats, you earned {new_score} points"
                f" obtaining the PyBites Ninja {belt.capitalize()} Belt"
            )
        else:
            message = f"Set new score to {new_score}"
        print(message)
        self._score = new_score

    score = property(_get_score, _set_score)
