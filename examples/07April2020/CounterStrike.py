energy = int(input())

won = 0

while True:
    distance = input()
    if distance == 'End of battle':
        print(f'Won battles: {won}. Energy left: {energy}')
        break

    distance = int(distance)

    if energy >= distance:
        energy -= distance
        won += 1
        if won % 3 == 0:
            energy += won
    else:
        print(f'Not enough energy! Game ends with {won} won battles and {energy} energy')
        break
