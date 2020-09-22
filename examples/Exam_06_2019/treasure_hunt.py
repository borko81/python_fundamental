treasure_chest = input().split('|')

while True:
    line = input()
    if line == 'Yohoho!':
        break

    line = line.split()
    if line[0] == 'Loot':
        for i in line[1:]:
            if i not in treasure_chest:
                treasure_chest.insert(0, i)

    elif line[0] == 'Drop':
        position = int(line[1])
        if 0 <= position <= len(treasure_chest):
            temp = treasure_chest.pop(position)
            treasure_chest.append(temp)

    elif line[0] == 'Steal':
        elements = int(line[1])
        print(", ".join([i for i in treasure_chest[-elements:]]))
        del treasure_chest[-elements:]

if len(treasure_chest) > 0:
    averageGain = sum(len(i) for i in treasure_chest) / len(treasure_chest)
    print(f'Average treasure gain: {averageGain:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
