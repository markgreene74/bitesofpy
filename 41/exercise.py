import functools

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    '''Make sure user is logged in before proceeding'''
    @functools.wraps(func)
    def wrapper_login_required(username):
        if username in loggedin_users:
            pass
        elif username in known_users:
            return 'please login'
        else:
            return 'please create an account'
        return func(username)
    return wrapper_login_required


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'