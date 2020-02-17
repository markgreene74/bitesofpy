# https://codechalleng.es/bites/40/
def binary_search(sequence, target):
    # define the uppper/lower limits
    low = 0
    high = len(sequence) - 1
    # start the search
    while low <= high:
        # pick the middle
        middle = (low + high) // 2
        # now start the search
        if sequence[middle] == target:
            # found it
            return middle
        elif sequence[middle] > target:
            # it's in the lower half, discard the upper half
            high = middle - 1
        else:
            # it must be in the upper half, discard the lower half
            low = middle + 1
    # if we made it to this point the target is not in the sequence
    return None

'''
Resolution time: ~50 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 12 min. 💪
'''
