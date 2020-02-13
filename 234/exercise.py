# https://codechalleng.es/bites/234/
import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = re.findall(r"(.+?[.?!]\s?)", text, re.MULTILINE)
    return "".join([sentence.capitalize() for sentence in sentences])

'''
Resolution time: ~40 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 19 min. 💪
'''
