from itertools import cycle

def sequence_generator():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # d = {}
    # for i, letter in enumerate(letters):
    #     d[i+1] = letter
    l = []
    for i, letter in enumerate(letters):
        l.append(i+1)
        l.append(letter)
    return cycle(l)