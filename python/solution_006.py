import time


def sum_of_squares(number):
    sum = 0
    for i in range(number + 1):
        sum += i * i
    return sum


def square_of_num(number):
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum**2


def solution():
    num = 100
    difference = square_of_num(num) - sum_of_squares(num)
    return difference


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")
