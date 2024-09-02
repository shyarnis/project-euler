import time


# Euclidean algorithm to find GCD.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def solution():
    result = 1

    for i in range(2, 21):
        result = lcm(result, i)

    return result


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")
