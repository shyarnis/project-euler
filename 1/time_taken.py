import time 

BIG_INTEGER = 19_000_000
result = 0

t1 = time.time()
for i in range(1, BIG_INTEGER):
    if i%3==0 or i%5==0:
        result += i
t2 = time.time()

print("Method 1")
print(f"Result: {result}")
print(f"Time Taken: {(t2-t1):.3f} seconds")


t1 = time.time()
def sum_divisible_by(n):
    p = BIG_INTEGER // n 
    return (n*(p*(p+1))) // 2

result = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
t2 = time.time()

print()
print("Method 2")
print(f"Result: {result}")
print(f"Time Taken: {(t22-t11):.3f} seconds")

