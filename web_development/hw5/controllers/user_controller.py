import re

from web_development.hw5.db import SQLiteClient
from web_development.hw5.models import User

INVALID_INPUT_MESSAGE = 'Invalid input'
EMPTY_INPUT_MESSAGE = 'Invalid input: cannot be empty. Please try again...'
INVALID_LOGIN_ATTEMPTS = 2
DB_CLIENT = SQLiteClient('.data/users.db')


def init_db():
    meta = {
        'user_id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'username': 'TEXT UNIQUE NOT NULL',
        'password': 'TEXT',
        'email': 'TEXT UNIQUE NOT NULL',
    }

    DB_CLIENT.create_table('users', meta)


def main_loop():
    options = [(1, 'LOGIN'), (2, 'REGISTER'), (3, 'EXIT')]
    while True:
        print('\n--- MAKE YOUR CHOICE! --- ')
        for o in options:
            print(f'{o[0]}: {o[1]}')

        selected_opt = option_input()

        match selected_opt:
            case 1:
                login_loop()
            case 2:
                registration_loop()
            case 3:
                print('\n--- BYE! --- ')
                break
            case _:
                print(f'\n--- ERROR ----\n{INVALID_INPUT_MESSAGE.upper()}: No such option!')

def option_input() -> int:
    while True:
        try:
            option = int(input('Enter an option: '))
            return option
        except ValueError as err:
            print('Invalid option. Try again.')


def login_loop() -> bool:
    print('\n--- USER LOGIN ---')

    DB_CLIENT.verify_connect()
    invalid_username_input_cnt = INVALID_LOGIN_ATTEMPTS
    while True:
        name = username_input()
        user_row = DB_CLIENT.fetch_one(f'SELECT * FROM users WHERE username = ?', (name,))

        if user_row:
            break
        elif invalid_username_input_cnt == 0:
            print('3 invalid username attempts! Exiting...')
            print('--- USER LOGIN FAILED ---')
            return False
        else:
            print('No such user found! Try again with a different username')
            invalid_username_input_cnt -= 1

    user_data = dict(zip(user_row.keys(), user_row))
    pwd_stored = user_data.get('password')
    pwd_input = password_input()
    pwd_match = pwd_input == pwd_stored

    if not pwd_match:
        invalid_pwd_input_cnt = 2

        while invalid_pwd_input_cnt > 0:
            print(f'Sorry, try again...\nYou have {invalid_pwd_input_cnt} attempts left')
            invalid_pwd_input_cnt -= 1
            pwd_input = password_input()
            pwd_match = pwd_input == pwd_stored

            if pwd_match:
                break

    if pwd_match:
        show_welcome_logo()
        print(f'\n Welcome, {user_data.get('username')}!!!  Your user_id is {user_data.get("user_id")}\n')
        print('--- USER LOGIN COMPLETED ---')
        return True
    else:
        print('3 incorrect password attempts! Exiting...')
        print('--- USER LOGIN FAILED ---')
        return False


def email_already_used(email) -> bool:
    DB_CLIENT.verify_connect()
    cnt = DB_CLIENT.fetch_one('SELECT COUNT(*) FROM users WHERE email = ?', (email,))[0]
    return cnt > 0


def registration_loop():
    print('\n--- USER REGISTRATION ---')

    while True:
        username = username_input()

        if user_exists(username):
            print(f'User {username} already exists!')
        else:
            break

    while True:
        email = email_input()

        if email_already_used(email):
            print(f'E-mail {email} is used by another user!')
        else:
            break

    password = password_input()
    user = User(username, email, password)

    DB_CLIENT.verify_connect()
    DB_CLIENT.insert('users', user.to_dict())

    db_user = User.from_dict(DB_CLIENT.fetch_one(f'SELECT * FROM users WHERE username = ?', (username,)))

    print(f'--- USER ADDED TO DATABASE: {db_user.to_dict()} ---: ')
    print('--- USER REGISTRATION COMPLETED ---')


def username_input() -> str:
    while True:
        try:
            username_in = input('Please enter username: ')

            if username_in.isdigit():
                raise TypeError(f'{INVALID_INPUT_MESSAGE}: digits username forbidden. Please try again...')
            elif username_in.strip() == "":
                raise ValueError(EMPTY_INPUT_MESSAGE)

            return username_in

        except (TypeError, ValueError) as err:
            print(err)


def email_input() -> str:
    while True:
        try:
            email_in = input('Please enter email: ')

            if email_in.strip() == "":
                raise ValueError(EMPTY_INPUT_MESSAGE)
            elif not is_valid_email(email_in):
                raise ValueError(f'{INVALID_INPUT_MESSAGE}: does not match email pattern! Please try again...')

            return email_in

        except (TypeError, ValueError) as err:
            print(err)


def password_input() -> str:
    while True:
        try:
            password_in = input('Please enter password: ')

            if password_in.strip() == "":
                raise ValueError(EMPTY_INPUT_MESSAGE)
            elif len(password_in) < 4:
                raise ValueError(
                    f'{INVALID_INPUT_MESSAGE}: password must be at least 4 characters long. Please try again...')
            return password_in
        except (TypeError, ValueError) as err:
            print(err)


def user_exists(username) -> bool:
    DB_CLIENT.verify_connect()
    cnt = DB_CLIENT.fetch_one(f'SELECT COUNT(*) FROM users WHERE username = ?', (username,))[0]
    return cnt > 0


def is_valid_email(email_in: str) -> bool:
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(regex, email_in):
        return True
    else:
        return False


def show_welcome_logo():
    logo = r"""
 __        __   _                                  
 \ \      / /__| | ___ ___  _ __ ___   ___   
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
   \ V  V /  __/ | (_| (_) | | | | | |  __/
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___| 
    """
    print(logo)
