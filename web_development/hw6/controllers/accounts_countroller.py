import re
from sqlalchemy import func

from ._constants import EMPTY_INPUT_MESSAGE, INVALID_INPUT_MESSAGE
from web_development.hw6.db_utils import Session
from web_development.hw6.models import SiteAccountData
from web_development.hw6.models.types import LoginType
from web_development.hw5.controllers.user_controller import email_input, password_input, option_input


def add_account_data(user_id) -> bool:
    site_url = url_input()
    acct_type = select_account_type_loop()
    site_login = email_input()

    if acct_type in (LoginType.google, LoginType.apple, LoginType.facebook):
        account_record = SiteAccountData(
            user_id=user_id,
            site_url=site_url,
            login_type=acct_type,
            login_user_name=site_login
        )
    else:
        pwd = password_input()
        account_record = SiteAccountData(
            user_id=user_id,
            site_url=site_url,
            login_type=acct_type,
            login_user_name=site_login,
            login_password=pwd
        )

    with Session() as session:
        cnt = session \
            .query(func.count(SiteAccountData.record_id)) \
            .filter_by(user_id=user_id, site_url=site_url, login_user_name=site_login) \
            .scalar()

        if cnt > 0:
            return False

        session.add(account_record)
        session.commit()

    return True


def print_accounts_by_user(user_id) -> None:
    with Session() as session:
        accounts = session.query(SiteAccountData).filter(SiteAccountData.user_id == user_id).all()

    print("--- Your current accounts: ---")
    for account in accounts:
        print(account.to_dict())


def select_account_action(user_id):
    options = [
        (1, 'ADD NEW ACCOUNT'),
        (2, 'VIEW ACCOUNTS'),
        (3, 'LOGOUT'),
    ]

    while True:
        print('\n--- PLEASE SELECT OPTION ---')

        for o in options:
            print(f'{o[0]}: {o[1]}')

        selected_opt = option_input()

        match selected_opt:
            case 1:
                add_account_data(user_id)
            case 2:
                print_accounts_by_user(user_id)
            case 3:
                print('BYE!')
                break
            case _:
                print(f'\n--- ERROR ----\n{INVALID_INPUT_MESSAGE.upper()}: No such option!')


def select_account_type_loop() -> LoginType:
    options = [
        (1, LoginType.apple.value),
        (2, LoginType.google.value),
        (3, LoginType.facebook.value),
        (4, LoginType.email.value),
    ]

    while True:
        print('\n--- PLEASE SELECT LOGIN TYPE ---')

        for o in options:
            print(f'{o[0]}: {o[1]}')

        selected_opt = option_input()

        match selected_opt:
            case 1:
                return LoginType.apple
            case 2:
                return LoginType.google
            case 3:
                return LoginType.facebook
            case 4:
                return LoginType.email
            case _:
                print(f'\n--- ERROR ----\n{INVALID_INPUT_MESSAGE.upper()}: No such option!')


def url_input() -> str:
    while True:
        try:
            url_in = input('Please enter url: ')

            if url_in.strip() == "":
                raise ValueError(EMPTY_INPUT_MESSAGE)
            elif not is_valid_url(url_in):
                raise ValueError(
                    f'{INVALID_INPUT_MESSAGE}:'
                    f' does not match url pattern ("https://<your address> or ftp://<your address>")!'
                    f'\nPlease try again...'
                )

            return url_in

        except (TypeError, ValueError) as err:
            print(err)


def is_valid_url(url: str) -> bool:
    regex = r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$'

    if re.match(regex, url):
        return True
    else:
        return False
