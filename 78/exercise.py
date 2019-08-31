def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    all = set([x for y in programmers.values() for x in y])
    return all.intersection(*programmers.values())
