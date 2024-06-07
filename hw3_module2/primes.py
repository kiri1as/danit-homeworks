import time
from threading import Thread
from multiprocessing import Process, Manager

from colorama import Fore, Style


def timing_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time_ns()
        result = func(*args, **kwargs)
        elapsed_time = time.time_ns() - start_time
        print(f'\n{Fore.BLUE}Function "{func.__name__}" executed in: {Fore.GREEN}{elapsed_time}ns {Style.RESET_ALL}')
        return result

    return wrapper


def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(start: int, end: int, results: list[int] = None):
    if results is None:
        results = []

    for x in range(start, end + 1):
        if is_prime(x):
            results.append(x)
    return results


@timing_log
def find_primes_single_thread(start, end):
    results = []
    t = Thread(target=find_primes, args=(start, end, results), daemon=True)
    t.start()
    t.join()
    return results


@timing_log
def find_primes_multi_thread(start, end):
    midpoint = (start + end) // 2
    results_first = []
    results_second = []

    t1 = Thread(target=find_primes, args=(start, midpoint, results_first), daemon=True)
    t2 = Thread(target=find_primes, args=(midpoint + 1, end, results_second), daemon=True)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return [*results_first, *results_second]


@timing_log
def find_primes_multi_process(start, end):
    midpoint = (start + end) // 2
    manager = Manager()
    results_first = manager.list()
    results_second = manager.list()

    p1 = Process(target=find_primes, args=(start, midpoint, results_first), daemon=True)
    p2 = Process(target=find_primes, args=(midpoint + 1, end, results_second), daemon=True)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    return list(results_first) + list(results_second)
