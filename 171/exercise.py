from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    t_end = time() + seconds
    for i in cycle(SPINNER_STATES):
        if time() < t_end:
            sys.stdout.write("\r{0}".format(i))
            sys.stdout.flush()
            sleep(STATE_TRANSITION_TIME)
        else:
            break


if __name__ == '__main__':
    spinner(2)