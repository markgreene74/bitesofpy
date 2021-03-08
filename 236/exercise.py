# https://codechalleng.es/bites/236/
# https://docs.python.org/3/library/difflib.html#difflib.get_close_matches
from pathlib import PosixPath
import difflib


def get_matching_files(directory: PosixPath, filter_str: str) -> list:
    """Get all file names in "directory" and (case insensitive) match the ones
    that exactly match "filter_str"

    In case there is no exact match, return closely matching files.
    If there are no closely matching files either, return an empty list.
    (Return file names, not full paths).

    For example:

    d = Path('.')
    files in dir: bite1 test output

    get_matching_files(d, 'bite1') => ['bite1']
    get_matching_files(d, 'Bite') => ['bite1']
    get_matching_files(d, 'pybites') => ['bite1']
    get_matching_files(d, 'test') => ['test']
    get_matching_files(d, 'test2') => ['test']
    get_matching_files(d, 'output') => ['output']
    get_matching_files(d, 'o$tput') => ['output']
    get_matching_files(d, 'nonsense') => []
    """
    list_of_files = [file.name for file in directory.iterdir()]
    a_match = difflib.get_close_matches(filter_str.lower(), list_of_files, 1, 1)
    if a_match:
        return a_match
    else:
        a_match = difflib.get_close_matches(
            filter_str.lower(), list_of_files, cutoff=0.75
        )
    if a_match:
        return a_match
    else:
        return difflib.get_close_matches(filter_str.lower(), list_of_files)
