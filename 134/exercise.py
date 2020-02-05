# https://codechalleng.es/bites/134/
def two_sums(numbers: list, target: int) -> tuple:
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    list_sums = [
        (i, j)
        for i, ii in enumerate(numbers)
        for j, jj in enumerate(numbers)
        if ii + jj == target
    ]

    if len(list_sums) == 0:  # no solution
        return None

    return sorted(list_sums, key=lambda x: numbers[x[0]])[0]

'''
Resolution time: ~42 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 16 min. 💪
'''
