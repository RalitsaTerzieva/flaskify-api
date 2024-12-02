from user import User

users = [
    User(1, 'Jose', 'mypassword'),
    User(2, 'David', 'password')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# check if user exists, if so, return user
def authenticate(username, password):

    user = username_table.get(username, None) # we use get because if there is no user we don't want an error
    if user and password == user.password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
