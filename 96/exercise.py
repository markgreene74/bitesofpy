def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        file_data = f.read()
    nl = '\n'
    return f"{len(file_data.split(nl))} {len(file_data.split())} {len(file_data)} {str(file_)}"