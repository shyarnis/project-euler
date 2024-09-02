from math import sqrt


def sieve_of_erathosthenes():
    limit = 200

    # set all numbers within limit are prime
    sieve = [1] * limit

    # 0 and 1 are not prime numbers.
    sieve[0] = 0
    sieve[1] = 0

    # implement sieve of erathosthenes
    sqrt_num = int(sqrt(limit))
    for i in range(2, sqrt_num + 1):
        if sieve[i] == 1:
            for j in range(i * i, limit, i):
                sieve[j] = 0  # <-- that is composite number

    # 1 indicates prime number
    total_sum = sum(i for i in range(2, limit) if sieve[i] == 1)

    return total_sum


print(sieve_of_erathosthenes())
