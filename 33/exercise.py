def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) == dict:
        first = (x for x in data.keys())
        second = (data[x] for x in data.keys())
        return [tuple(first), tuple(second)]
    elif type(data) == list:
        list_names = []
        list_since = []
        list_karma = []
        list_bitecoin = []
        for item in data:
            list_names.append(item.name)
            list_since.append(item.since_days)
            list_karma.append(item.karma_points)
            list_bitecoin.append(item.bitecoin_earned)
        return [tuple(list_names), tuple(list_since), tuple(list_karma), tuple(list_bitecoin)]