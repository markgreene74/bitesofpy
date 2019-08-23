import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    n_dirs = 0
    n_files = 0
    for root, dirs, files in os.walk(directory):
        n_dirs += len(dirs)
        n_files += len(files)
    return (n_dirs, n_files)