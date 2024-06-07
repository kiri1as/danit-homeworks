import pytest

from primes import find_primes, find_primes_single_thread, find_primes_multi_thread, find_primes_multi_process


# Для пошуку простих чисел в маленькому діапазоні немає сенсу створювати потоки або процеси.
# Якщо пошук здійснюється серед великої кількості чисел, то тут набагато ефективнішим буде використовувати потоки або процеси.
# Проте при використанні процесів є витрати на їх створення та об'єднаня списків з різних просторів пам'яті (у потоків він один),
# тому на різних об'ємах даних буде різна ефекивність.

@pytest.mark.parametrize(
    "test_start, test_end, expected_lst",
    [
        (50, 100, [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
        (78, 300,
         [79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
          197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
         ),
    ]
)
def test_find_primes(test_start, test_end, expected_lst):
    assert find_primes(test_start, test_end) == expected_lst


@pytest.mark.parametrize(
    "test_start, test_end, expected_lst",
    [
        (50, 100, [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
        (78, 300,
         [79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
          197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
         ),
    ]
)
def test_find_primes_equal_results_threads(test_start, test_end, expected_lst):
    assert find_primes_single_thread(test_start, test_end) == expected_lst
    assert find_primes_multi_thread(test_start, test_end) == expected_lst
    assert find_primes_multi_process(test_start, test_end) == expected_lst
