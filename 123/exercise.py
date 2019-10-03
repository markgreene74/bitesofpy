from collections import Counter, defaultdict

names = "bob julian tim martin rod sara joyce nick beverly kevin".split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (5, 9),
    (6, 8),
    (7, 8),
    (8, 9),
]


def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    # build a dict of whos's friend with whom
    d = defaultdict(list)
    for k, v in users.items():
        # this gives us a list of tuples
        alist = [i for i in friendships if k in i]
        # let's split the tuples in two lists
        list1, list2 = zip(*alist)
        d[v] = [users[i] for i in list1 + list2 if i != k]
    # now let's find the most popular
    c = Counter()
    for i in friendships:
        c.update(i)
    # most_common() returns a list which
    # consists of a tuple: [(5, 4)]
    most_popular_id = c.most_common(1)[0][0]
    name = users[most_popular_id]
    return (name, d[name])
