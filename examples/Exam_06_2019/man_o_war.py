pirate = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
p_health = int(input())

defeat = False

while True:
    line = input()
    if line == 'Retire':
        break

    line = line.split()
    if line[0] == 'Fire':
        position = int(line[1])
        damage = int(line[2])

        if 0 <= position <= len(warship):
            warship[position] -= damage
            if warship[position] <= 0:
                print('You won! The enemy ship has sunken.')
                defeat = True
                break

    elif line[0] == 'Defend':
        start = int(line[1])
        end = int(line[2])
        damage = int(line[3])

        if 0 <= start <= end < len(pirate):
            for d in range(start, end+1):
                pirate[d] -= damage
                if pirate[d] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    defeat = True
                    break

    elif line[0] == 'Repair':
        index = int(line[1])
        health = int(line[2])
        if 0 <= index < len(pirate):
            pirate[index] += health
            if pirate[index] > p_health:
                pirate[index] = p_health

    elif line[0] == 'Status':
        count = len([i for i in pirate if i < p_health * 0.2])
        print(f'{count} sections need repair.')


if defeat is False:
    print(f"Pirate ship status: {sum(pirate)}")
    print(f"Warship status: {sum(warship)}")
