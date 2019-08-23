def get_profile(name: str, age: int, *args, **kwargs):
    if not type(age) == int:
        raise ValueError("age must be an integer")
    if len(args) > 5:
        raise ValueError("max 5 args required")
    result = {}
    result['name'] = name
    result['age'] = age
    if args:
        result['sports'] = sorted(list(args))
    if kwargs:
        result['awards'] = kwargs
    return result