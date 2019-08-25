from statistics import mean


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    return [round(mean(sequence[: x + 1]), 2) for x in range(len(sequence))]
