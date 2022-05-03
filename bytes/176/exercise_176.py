WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""
    half = int(size / 2)
    twin = WHITE + BLACK
    reverse_twin = BLACK + WHITE
    for i in range(half):
        print(f"{twin * half}")
        print(f"{reverse_twin * half}")
