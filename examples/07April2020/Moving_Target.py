targets = [int(x) for x in input().split()]


while True:
    command = input()
    if command == 'End':
        print("|".join(str(x) for x in targets))
        break

    elif command.startswith('Shoot'):
        _, index, power = command.split()
        index = int(index)
        power = int(power)

        if len(targets) > index >= 0:
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif command.startswith('Add'):
        _, index, value = command.split()
        index = int(index)
        value = int(value)
        if len(targets) > index >= 0:
            targets.insert(index, value)
        else:
            print('Invalid placement!')


    elif command.startswith('Strike'):
        _, index, radius = command.split()
        index = int(index)
        radius = int(radius)
        if  len(targets) > index >= 0 and index + radius < len(targets) and index - radius >= 0:
            del targets[index - radius:index+radius+1]
        else:
            print('Strike missed!')