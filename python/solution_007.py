import time
import math


def is_prime(number):
    sqrt_num = int(math.sqrt(number))

    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            return False

    return True


def solution():
    upper_bound = 250_000_000  # huge number needed.
    target_index = 10_001
    count = 0

    for i in range(2, upper_bound):
        if is_prime(i):
            count += 1

            if count == target_index:
                return i

    return -1


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")
