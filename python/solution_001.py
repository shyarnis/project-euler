import time


def solution() -> int:
    target = 1000
    sum = 0

    for i in range(1, target):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")


# Method 2
def sum_divisible_by(n):
    target = 999
    p = target // n
    return ((p * (p + 1)) * 0.5) * n


def solution2():
    sum = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
    return int(sum)
