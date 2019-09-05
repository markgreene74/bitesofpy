def flatten(list_of_lists):
    for i in list_of_lists:
        if type(i) == list or type(i) == tuple:
            yield from flatten(i)
        else:
            yield i
