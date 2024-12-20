import re
from sqlalchemy import func

from ._constants import EMPTY_INPUT_MESSAGE, INVALID_INPUT_MESSAGE
from .menu_controller import select_account_type_loop
from web_development.hw6.models.types import LoginType
from web_development.hw5.controllers.user_controller import email_input, password_input
from web_development.hw6.db_utils import Session
from web_development.hw6.models import SiteAccountData


def print_accounts_by_user(user_id) -> None:
    with Session() as session:
        accounts = session.query(SiteAccountData).filter(SiteAccountData.user_id == user_id).all()

    print("--- Your current accounts: ---")
    for account in accounts:
        print(account.to_dict())


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
            .query(func.count(SiteAccountData)) \
            .filter_by(user_id=user_id, site_url=site_url, site_login=site_login) \
            .scalar()

        if cnt > 0:
            return False

        session.add(account_record)
        session.commit()

    return True


def url_input() -> str:
    while True:
        try:
            url_in = input('Please enter url: ')

            if url_in.strip() == "":
                raise ValueError(EMPTY_INPUT_MESSAGE)
            elif not is_valid_url(url_in):
                raise ValueError(f'{INVALID_INPUT_MESSAGE}: does not match url pattern! Please try again...')

            return url_in

        except (TypeError, ValueError) as err:
            print(err)


def is_valid_url(url: str) -> bool:
    regex = r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$'

    if re.match(regex, url):
        return True
    else:
        return False
