import time


def is_palindrone(number):
    str_number = str(number)
    return str_number == str_number[::-1]


def solution():
    power = 3
    max_num = pow(10, power) - 1
    min_num = pow(10, power - 1)
    max_palindrome = 0

    for i in range(max_num, min_num, -1):
        for j in range(i, min_num, -1):
            product = i * j

            # since, j is decreasing, no need to check for smaller products.
            if product <= max_palindrome:
                break

            if is_palindrone(product):
                max_palindrome = product

    return max_palindrome


start = time.perf_counter()
ans = solution()
finish = time.perf_counter()
duration = finish - start

print(f"Answer     = {ans}")
print(f"Time Taken = {duration:.2f} seconds")
