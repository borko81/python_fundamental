targets = [int(x) for x in input().split()]

def shoot(targets, index, power):
    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
        return targets
    return targets


def add_to_targets(targets, index, value):
    if index in range(len(targets)):
        targets.insert(index, value)
        return targets
    else:
        print('Invalid placement!')
        return targets


def strike(targets, index, radios):
    if index + radios in range(len(targets)) and index - radios in range(len(targets)):
        targets = targets[0:index - radios] + targets[index+radios + 1:]
        return targets
    else:
        print('Strike missed!')
        return targets



while True:
    command = input().split()
    if command[0] == 'End':
        break

    elif command[0] == 'Shoot':
        _, index, power = command
        index = int(index)
        power = int(power)
        targets = shoot(targets, index, power)

    elif command[0] == 'Add':
        _, index, value = command
        index = int(index)
        value = int(value)
        targets = add_to_targets(targets, index, value)

    elif command[0] == 'Strike':
        _, index, radios = command
        index = int(index)
        radios = int(radios)
        targets = strike(targets, index, radios)


print("|".join(str(x) for x in targets))