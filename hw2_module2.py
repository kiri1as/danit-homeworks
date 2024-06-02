import atexit
import functools
import sys

import pytest
from colorama import Fore, Style


def log_error_exit(**kwargs):
    print(f'{Fore.RED}Function "{kwargs.get("func").__name__}" finished with error: {str(kwargs.get("err")).upper()}'
          f'{Fore.BLUE}\nExiting...{Style.RESET_ALL}')


def end_with_err_message(error):
    atexit.register(functools.partial(log_error_exit, func=log_error_exit, err=error))
    sys.exit(1)


class ParamsLog:
    def __init__(self, func):
        self.func = func
        functools.wraps(func)(self)

    def __call__(self, *args, **kwargs):
        print(f'\n{Fore.BLUE}Function "{self.func.__name__}" call:'
              f'{Fore.GREEN}\n\tparameters: {args}.'
              f'{Fore.GREEN}\n\tnamed params: {kwargs}'
              f'{Style.RESET_ALL}')
        return self.func(*args, **kwargs)


def check_division_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError as err:
            end_with_err_message(err)

    return wrapper


def check_index_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as err:
            end_with_err_message(err)

    return wrapper


@check_division_error
@ParamsLog
def divide(a, b):
    return a / b


@check_index_error
@ParamsLog
def get_element(lst, idx):
    return lst[idx]


# TESTS
@pytest.mark.parametrize(
    "a, b, expected", [(10, 5, 2), (50, 10, 5), (20, 0, 20)]
)
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_exits():
    with pytest.raises(SystemExit) as exit_info:
        divide(2, 0)
    assert exit_info.type == SystemExit
    assert exit_info.value.code == 1


@pytest.mark.parametrize(
    "test_list, test_index, expected_element",
    [
        (['a', 'b', 'c', 'd'], 2, 'c'),
        (['a', 'b', 'c', 'd'], 0, 'a'),
        (['a', 'b', 'c', 'd'], 4, 'b'),
        (['z', 'y', 'x', 'w'], 3, 'w'),
        (['z', 'y', 'x', 'w'], 1, 'y'),
        (['z', 'y', 'x', 'w'], -1, 'z'),
    ]
)
def test_get_element_normal(test_list, test_index, expected_element):
    assert test_list[test_index] == expected_element


def test_get_element_exits():
    with pytest.raises(SystemExit) as exit_info:
        get_element(['aaa', 'bbb', 'ccc', 'ddd', 'eee'], 10)
    assert exit_info.type == SystemExit
    assert exit_info.value.code == 1
