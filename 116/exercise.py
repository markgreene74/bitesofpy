import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    ls = os.listdir(dirname)
    return [
        file
        for file in ls
        if os.stat(os.path.join(dirname, file)).st_size >= size_in_kb * ONE_KB
    ]
