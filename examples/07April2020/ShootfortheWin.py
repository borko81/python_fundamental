targets = [int(x) for x in input().split()]

s = 0

while True:
    shot = input()
    if shot == 'End':
        print(f"Shot targets: {s} -> {' '.join(str(x) for x in targets)}")
        break

    shot = int(shot)
    if shot < len(targets):
        s += 1
        temp = targets[shot]
        targets[shot] = -1
        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            elif targets[i] > temp:
                targets[i] -= temp
            else:
                targets[i] += temp
