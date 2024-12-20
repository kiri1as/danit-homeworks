from ._constants import INVALID_INPUT_MESSAGE
from .accounts_countroller import add_account_data, print_accounts_by_user
from .user_controller import user_login_loop as login, user_registration_loop as register
from web_development.hw6.db_utils import close_all_sessions
from web_development.hw6.models.types import LoginType


def main_menu_loop():
    options = [(1, 'LOGIN'), (2, 'REGISTER'), (3, 'EXIT')]
    while True:
        print('\n--- MAKE YOUR CHOICE! --- ')
        for o in options:
            print(f'{o[0]}: {o[1]}')

        selected_opt = option_input()

        match selected_opt:
            case 1:
                login()
            case 2:
                register()
            case 3:
                close_all_sessions()
                print('BYE!')
                break
            case _:
                print(f'\n--- ERROR ----\n{INVALID_INPUT_MESSAGE.upper()}: No such option!')


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
                main_menu_loop()
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


def option_input() -> int:
    while True:
        try:
            option = int(input('Enter an option: '))
            return option
        except ValueError:
            print('Invalid option. Try again.')
