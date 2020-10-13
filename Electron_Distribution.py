n = 10

counter = 1
result = []

while n != 0:
    v = 2*(counter**2)
    if v < n:
        result.append(v)
        n -= v
    else:
        result.append(n)
        n = 0
    counter += 1

print(result)