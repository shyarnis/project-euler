import time


def solution() -> int:
    n = 600851475143
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")


# Method 2
def solution2():
    target = 600851475143
    i = 2

    while i * i < target:

        while target % i == 0:
            target /= i
        i += 1

    return int(target)
