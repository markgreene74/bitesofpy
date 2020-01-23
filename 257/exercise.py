# https://codechalleng.es/bites/257/
import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    result = dict()
    for line in passwd.splitlines():
        # not an empty line
        if len(line):
            sections = line.split(":")
            _name = sections[0].strip()
            _pass = re.sub(r",+", " ", sections[4]) or "unknown"
            result[_name] = _pass.strip()
    return result
