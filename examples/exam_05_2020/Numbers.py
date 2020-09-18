numbers = [int(x) for x in input().split()]

result = [x for x in numbers if x > sum(numbers)/len(numbers)]

if result:
    [print(x, end=' ') for x in (sorted(result, reverse=True)[0:5])]
else:
    print('No')