class RecordScore():

    """Class to track a game's maximum score"""

    def __init__(self):
        self.score = [0]

    def __call__(self, newscore):
        self.score.append(newscore)
        return max(self.score)

    def __str__(self):
        return ', '.join([str(i) for i in sorted(self.score, reverse=True)])

    def __repr__(self):
        return str(self.score)
