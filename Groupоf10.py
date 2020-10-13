from collections import defaultdict
numbers = [int(x) for x in input().split(', ')]
groups = defaultdict(list)

m = set()

for i in numbers:
    if 0 <= i <= 10:
        groups[10].append(i)
        m.add(10)
    elif 11 <= i <= 20:
        groups[20].append(i)
        m.add(20)
    elif 21 <= i <= 30:
        groups[30].append(i)
        m.add(30)
    elif 31 <= i <= 40:
        groups[40].append(i)
        m.add(40)
    elif 41 <= i <= 50:
        groups[50].append(i)
        m.add(50)
    elif 51 <= i <= 60:
        groups[60].append(i)
        m.add(60)


for i in range(10, max(m) + 10, 10):
    print(f'Group of {i}\'s: {groups[i]}')
