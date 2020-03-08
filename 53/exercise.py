# https://codechalleng.es/bites/53/
from textwrap import wrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    split_text = [i.strip() for i in text.split("\n\n")]
    text2col = [wrap(i.strip(), COL_WIDTH) for i in split_text]
    result = []
    for i in zip(*text2col):
        result.append("    ".join(i))
    return "".join(result)
