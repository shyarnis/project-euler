target = 999

def sum_divisible_by(n):
    p = target // n 
    return (n*(p*(p+1))) // 2

result = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
print(result)
