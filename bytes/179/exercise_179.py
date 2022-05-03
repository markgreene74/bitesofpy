# https://codechalleng.es/bites/179/
import re


def strip_comments(code):
    # see Bite description
    # remove '#' comments, single line and inline
    code = re.sub(r"#\s+.*\n\s*|\s\s#\s.*$", r"", code)
    # remove single line '"""' comments
    code = re.sub(r'\s+""".*"""', r"", code)
    # remove multiline '"""' comments
    code = re.sub(r'""".*"""\n\s*', r"", code, re.MULTILINE, re.DOTALL)
    return code
