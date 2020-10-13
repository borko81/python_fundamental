version = [int(x) for x in input().split('.')]


if version[-1] + 1 >= 10:
    version[-1] = 0
    version[-2] += 1
    if version[-2] >= 10:
        version[-2] = 0
        version[-3] += 1
else:
    version[-1] += 1

print(version)


