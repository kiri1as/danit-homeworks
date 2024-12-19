from ._constants import INVALID_INPUT_MESSAGE
from .user_controller import user_login_loop as login, user_registration_loop as register
from web_development.hw6.db_utils import close_all_sessions


def menu_loop():
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


def option_input() -> int:
    while True:
        try:
            option = int(input('Enter an option: '))
            return option
        except ValueError:
            print('Invalid option. Try again.')