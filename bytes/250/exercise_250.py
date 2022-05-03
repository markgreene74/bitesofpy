# https://codechalleng.es/bites/250/
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    if record == 0:
        return CODEX[0]
    partial = list()
    while record:
        record, rem = divmod(record, BASE)
        partial.append(CODEX[rem])
    partial.reverse()
    return "".join(partial)


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    url_lenght = len(short_url)
    result = 0
    _index = 0
    for i in short_url:
        power = url_lenght - (_index + 1)
        result += CODEX.index(i) * (BASE ** power)
        _index += 1
    return result


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    # check if it's a valid shorted URL
    if not (SITE in url):
        return INVALID
    # get the shortened portion, for example:
    # "https://pybit.es/e6" -> "e6"
    _shortened = url.replace(SITE, "").strip("/")
    # decode it
    _decoded = decode(_shortened)
    # try to get the full URL if it exists
    full_url = LINKS.get(_decoded)
    # return the full URL or the error message if
    # the URL is not stored in LINKS
    return full_url or NO_RECORD


def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    # encode next_record
    _encoded = encode(next_record)
    # save the URL in LINKS using next_record as the key
    LINKS[next_record] = url
    # return the shortened URL
    return f"{SITE}/{_encoded}"


"""
Resolution time: ~67 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 43 min. 💪
"""
