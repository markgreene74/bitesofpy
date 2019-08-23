from itertools import combinations, permutations

def friends_teams(friends_list: list, team_size: int, order_does_matter: bool = False):
    if order_does_matter:
        return permutations(friends_list, team_size)
    else:
        return combinations(friends_list, team_size)