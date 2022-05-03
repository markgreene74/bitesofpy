def get_profile(**kwargs):
    if len(kwargs) == 0:
        return "julian is a programmer"
    elif len(kwargs) == 1 and "name" in kwargs.keys():
        return f"{kwargs.get('name')} is a programmer"
    elif len(kwargs) == 2 and "name" in kwargs.keys() and "profession" in kwargs.keys():
        return f"{kwargs.get('name')} is a {kwargs.get('profession')}"
    else:
        raise TypeError
