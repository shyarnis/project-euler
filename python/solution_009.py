import time


def solution():
    target = 1000

    # a, b won't be less than 400.
    # pythagorean triplet begins from 3.
    for a in range(3, 400):
        for b in range(a + 1, 400):

            c = target - a - b

            if a < b < c and a**2 + b**2 == c**2:
                print(a, b, c)
                return a * b * c


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")
