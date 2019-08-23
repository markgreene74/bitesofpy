import itertools

def find_number_pairs(numbers, N=10):
    all_pairs = [x for x in itertools.combinations(numbers, 2)]
    return [x for x in all_pairs if (x[0]+x[1]) == N]