# https://codechalleng.es/bites/155/
import re


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    result = re.findall(r'(\w+|".*")', text)
    for i, j in enumerate(result):
        if '"' in j:
            result[i] = j.replace('"', "")
    return result
