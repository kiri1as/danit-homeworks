from web_development.hw6.db_utils import close_all_sessions
from ._constants import INVALID_INPUT_MESSAGE
from .accounts_countroller import select_account_action
from .user_controller import user_login_loop as user_login, user_registration_loop as register_loop
from web_development.hw5.controllers.user_controller import option_input


def main_menu_loop():
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
                register_loop()
            case 3:
                close_all_sessions()
                print('BYE!')
                break
            case _:
                print(f'\n--- ERROR ----\n{INVALID_INPUT_MESSAGE.upper()}: No such option!')


def login_loop():
    user_id = user_login()

    if user_id != -1:
        select_account_action(user_id)

