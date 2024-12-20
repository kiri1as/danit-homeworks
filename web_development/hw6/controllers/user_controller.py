from sqlalchemy import func

from web_development.hw5.controllers.user_controller import username_input, email_input, password_input
from web_development.hw6.db_utils import Session
from web_development.hw6.models import User


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
