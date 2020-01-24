# https://codechalleng.es/bites/163/
from collections import defaultdict


def parser_helper(reqs: str) -> dict:
    """Parse a requirement multiline string and
       return a dictionary of packages as keys
       and version (tuple) as value
    """
    result = defaultdict(tuple)
    for pkg in reqs.strip().splitlines():
        _name, _version = pkg.split("==")
        _version_tuple = tuple(int(i) for i in _version.split("."))
        result[_name] = _version_tuple
    return result


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    result = []
    old = parser_helper(old_reqs)
    new = parser_helper(new_reqs)
    for pkg_name, old_version in old.items():
        if new.get(pkg_name) > old_version:
            result.append(pkg_name)
    return result

'''
Resolution time: ~54 min. (...) - awesome, you solved it in 26 min. 💪
'''
