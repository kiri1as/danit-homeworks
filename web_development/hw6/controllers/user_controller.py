from web_development.hw5.controllers.user_controller import username_input, email_input, password_input


def user_login_loop():
    pass

def user_registration_loop():
    print('\n--- USER REGISTRATION ---')

    while True:
        username = username_input()

        if _user_exists(username):
            print(f'User {username} already exists!')
        else:
            break

    while True:
        email = email_input()

        if _email_already_used(email):
            print(f'E-mail {email} is used by another user!')
        else:
            break

    password = password_input()
    # user = User(username, email, password)

    # DB_CLIENT.verify_connect()
    # DB_CLIENT.insert('users', user.to_dict())

    # db_user = User.from_dict(DB_CLIENT.fetch_one(f'SELECT * FROM users WHERE username = ?', (username,)))

    # print(f'--- USER ADDED TO DATABASE: {db_user.to_dict()} ---: ')
    # print('--- USER REGISTRATION COMPLETED ---')


def _user_exists(username) -> bool:
    return True
    # DB_CLIENT.verify_connect()
    # cnt = DB_CLIENT.fetch_one(f'SELECT COUNT(*) FROM users WHERE username = ?', (username,))[0]
    # return cnt > 0

def _email_already_used(email) -> bool:
    return True
    # DB_CLIENT.verify_connect()
    # cnt = DB_CLIENT.fetch_one('SELECT COUNT(*) FROM users WHERE email = ?', (email,))[0]
    # return cnt > 0
