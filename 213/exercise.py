# https://codechalleng.es/bites/213/
import re


def find_text(aregex, or_text, tr_text):
    def get_or():
        return re.findall(aregex, or_text, re.MULTILINE | re.DOTALL)

    def get_tr():
        return re.findall(aregex, tr_text, re.MULTILINE | re.DOTALL)

    return (get_or(), get_tr()) if get_or() else (False, False)


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    strings_code_or, strings_code_tr = find_text(
        r"code>(.+?\n*.+?)<\/code", org_text, trans_text
    )
    strings_pre_or, strings_pre_tr = find_text(
        r"pre>(.+?\n*.+?)<\/pre", org_text, trans_text
    )

    if strings_code_or:
        for i, text in enumerate(strings_code_or):
            trans_text = trans_text.replace(strings_code_tr[i], text)

    if strings_pre_or:
        for i, text in enumerate(strings_pre_or):
            trans_text = trans_text.replace(strings_pre_tr[i], text)

    return trans_text
