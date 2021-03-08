NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    newlist = []
    for name in names:
        titlecase = " ".join([x.capitalize() for x in name.split()])
        if titlecase not in newlist:
            newlist.append(titlecase)
    return newlist


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_list = []
    # get a sorted list of lastnames
    lastnames = sorted([x.split()[1] for x in names], reverse=True)
    # for each lastnames find the corresponding entry
    # and add it to sorted_list
    for i in lastnames:
        sorted_list.append([y for y in names if i in y][0])
    return sorted_list


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # extract first names
    firstnames = [x.split()[0] for x in names]
    d = {}
    # create a dictionary with the lenght of name
    # as key
    for i in firstnames:
        d[len(i)] = i
    # sorted(d) returns a list, sorted(d)[0] is
    # the key corresponding to the shortest name
    return d[sorted(d)[0]]
