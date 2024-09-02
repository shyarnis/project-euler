import time
from math import sqrt


def solution():
    limit = 2_000_000
    sieve = [None] * limit

    # assume all numbers are prime number(i.e set 1) within limit
    for i in range(2, limit):
        sieve[i] = 1

    # implement sieve of erathosthenes
    sqrt_num = int(sqrt(limit))
    for i in range(2, sqrt_num + 1):
        if sieve[i] == 1:
            for j in range(i * i, limit, i):
                sieve[j] = 0

    # add all index from sieve whose value is 1
    # 1 indicates it is prime number index.
    sum = 0
    for i in range(2, limit):
        if sieve[i] == 1:
            sum += i

    return sum


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")
