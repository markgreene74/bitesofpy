# https://codechalleng.es/bites/245/
STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
    for given rows of leafs (default 10).
    For more information see the test and the bite description"""
    tree = f'{" " * (rows - 1)}{STAR}'
    for i in range(rows + 1):
        tree += f'{" " * (rows - i)}{LEAF * (i * 2 - 1)}'.rstrip() + "\n"
    _max_leafs = rows * 2 - 1
    _trunk = int(round(_max_leafs / 2) + 1)
    tree += f'{" " * int(_max_leafs / 4)}{TRUNK * _trunk}\n'
    tree += f'{" " * int(_max_leafs / 4)}{TRUNK * _trunk}\n'
    return tree.strip("\n")
