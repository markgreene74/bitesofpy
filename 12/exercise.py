from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    def __init__(self, message):
        self.message = message

class UserAccessExpired(Exception):
    def __init__(self, message):
        self.message = message

class UserNoPermission(Exception):
    def __init__(self, message):
        self.message = message

def get_secret_token(username):
    names_list = [getattr(x, 'name') for x in USERS]
    if username in names_list:
        for a_user in USERS:
            if a_user.name == username:
                u_name, u_role, u_expired = a_user
                check_role = True if u_role == ADMIN else False
                if check_role and not u_expired:
                    return SECRET
                elif u_expired:
                    raise UserAccessExpired(f'{username}: user expired')
                elif not check_role:
                    raise UserNoPermission(f'{username}: user role is not {ADMIN}')
    else:
        raise UserDoesNotExist(f'{username}: user does not exist')