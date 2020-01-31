# https://codechalleng.es/bites/146/
STAR = "*"
BLANK = " "


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    # assume width is odd as per the exercise
    top_half = []

    for i in range(1, width + 2, 2):
        margin = int((width - i) / 2)
        top_half.append(f"{margin * BLANK}{i * STAR}{margin * BLANK}")

    bottom_half = top_half[-2::-1]
    return top_half + bottom_half

'''
Resolution time: ~58 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 19 min. 💪
'''
