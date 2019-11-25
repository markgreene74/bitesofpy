# https://codechalleng.es/bites/76/
from functools import singledispatch


@singledispatch
def count_down(arg):
    # TODO: Learn how to use singledispatch!
    raise ValueError("Wrong type!")


@count_down.register(int)
@count_down.register(str)
@count_down.register(float)
def _(arg):
    astr = str(arg)
    for i in range(len(astr), 0, -1):
        print("".join(astr[:i]))


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(dict)
@count_down.register(range)
def _(arg):
    astr = "".join([str(i) for i in arg])
    for i in range(len(astr), 0, -1):
        print("".join(astr[:i]))


# if you like me would like to exclude the '.'
# @count_down.register(float)
# def _(arg):
#     astr = str(arg).replace(".", "")
#     for i in range(len(astr), 0, -1):
#         print("".join(astr[:i]))
