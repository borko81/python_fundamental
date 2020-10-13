numbers = [int(x) for x in input().split(', ')]

result = [pos for pos, i in enumerate(numbers) if i % 2 == 0]

print(result)