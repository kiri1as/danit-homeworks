import numpy as np

if __name__ == "__main__":
    arr1 = np.random.randint(0, 10, size=(5, 5), dtype=np.int64)
    arr2 = np.random.randint(0, 10, size=(5, 5), dtype=np.int64)
    sum1 = arr1.sum()
    sum2 = arr2.sum()
    diff_arr = arr1 - arr2
    mult_arr = arr1 * arr2
    power_arr = arr1 ** arr2

    print(f"\nRandom numbers array 1:\n{arr1}")
    print(f"\nRandom numbers array 2:\n{arr2}\n")

    print(f"Array 1 sum: {sum1}")
    print(f"Array 2 sum: {sum2}")
    print(f"\nDifference array (arr1 - arr2):\n{diff_arr}")
    print(f"\nMultiply array (arr1 * arr2):\n{mult_arr}")
    print(f"\nPower array (arr1 ** arr2):\n{power_arr}")
