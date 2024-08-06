import time


def solution() -> int:
    target = 4_000_000
    sum = 0
    a = 0
    b = 1

    while a < target:
        if a % 2 == 0:
            sum += a

        # swap
        a, b = b, a + b

    return sum


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")


# Method 2
def solution2():
    target = 4_000_000
    sum = 0
    a = 1
    b = 1
    c = a + b

    while c < target:
        sum += c
        a = b + c
        b = c + a
        c = a + b

    return sum
