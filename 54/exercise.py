from textwrap import TextWrapper, dedent

INDENTS = 4


def print_hanging_indents(poem):
    wrapper = TextWrapper(subsequent_indent=" " * INDENTS, width=50)
    for i in poem.split("\n\n"):
        print("\n".join(wrapper.wrap(i.strip())))
