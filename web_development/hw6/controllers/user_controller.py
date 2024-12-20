from sqlalchemy import func

from web_development.hw5.controllers.user_controller import username_input, email_input, password_input, \
    show_welcome_logo
from web_development.hw6.controllers._constants import INVALID_LOGIN_ATTEMPTS
from web_development.hw6.db_utils import Session
from web_development.hw6.models import User


def user_login_loop() -> int:
    print('\n--- USER LOGIN ---')

    invalid_username_input_cnt = INVALID_LOGIN_ATTEMPTS

    while True:
        name = username_input()
        with Session() as session:
            user = session.query(User).filter(User.username == name).first()

        if user:
            break
        elif invalid_username_input_cnt == 0:
            print('3 invalid username attempts! Exiting...')
            print('--- USER LOGIN FAILED ---')
            return False
        else:
            print('No such user found! Try again with a different username')
            invalid_username_input_cnt -= 1

    pwd_stored = user.password
    pwd_input = password_input()

    if not pwd_input == pwd_stored:
        invalid_pwd_input_cnt = 2

        while invalid_pwd_input_cnt > 0:
            print(f'Sorry, try again...\nYou have {invalid_pwd_input_cnt} attempts left')
            invalid_pwd_input_cnt -= 1
            pwd_input = password_input()

            if pwd_input == pwd_stored:
                break


    if pwd_input == pwd_stored:
        show_welcome_logo()
        print(f'\n Welcome, {user.username}!!!  Your user_id is {user.user_id}\n')
        print('--- USER LOGIN COMPLETED ---')
        return user.user_id
    else:
        print('3 incorrect password attempts! Exiting...')
        print('--- USER LOGIN FAILED ---')
        return -1


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
    user = User(username=username, email=email, password=password)
    with Session() as session:
        session.add(user)
        session.commit()
        db_user = session.query(User).filter_by(username=username).first()

    print(f'--- USER ADDED TO DATABASE: {db_user.to_dict()} --- ')
    print('--- USER REGISTRATION COMPLETED ---')


def _user_exists(username) -> bool:
    with Session() as session:
        cnt = session.query(func.count(User.user_id)).filter_by(username=username).scalar()
    return cnt > 0


def _email_already_used(email) -> bool:
    with Session() as session:
        cnt = session.query(func.count(User.user_id)).filter_by(email=email).scalar()
    return cnt > 0
