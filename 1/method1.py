result = 0
for i in range(1, 1000):
    if i%3==0 or i%5==0:
        result += i
print(result)


# list comphrension
result = [i for i in range(1000) if i%3==0 or i%5==0]
print(sum(result))

# one liner
#print(sum([i for i in range(1000) if i%3==0 or i%5==0]))
