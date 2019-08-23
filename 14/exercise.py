import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*stuff):
    newstuff = zip(*stuff)
    for item in newstuff:
        yield SEPARATOR.join([str(x) for x in item])