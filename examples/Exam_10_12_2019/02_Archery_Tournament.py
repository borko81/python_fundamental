'''
    • "Shoot Left@{start index}@{length}":
    • Iskren starts traversing the archery field to the left from {start index} with given {length}.
    • If he goes out of the field, he will continue from the end of the field.
    • "Shoot Right@{start index}@{length}":
    • Iskren starts traversing the archery field to the right from {start index} with given {length}.
    • If he goes out of the field, he will continue from the start of the field.
    • "Reverse":
Reverse the archery field.
    • "Game Over"
Print the archery field and collected points.
When he arrives at the target, he will shoot at it and increase his points by 5 and decrease the target by 5 points,
if the target points are less than 5, he takes all of them and decreases it to 0. If the start index is out of range
of the field Iskren will have to ignore the command.
'''

targets = [int(x) for x in input().split('|')]
points = 0

'''
target1 = (2 - n) % len(a)
target2 = (2 + n) % len(a)
'''

def calc_rigth_position(start_position, target):
    # Right
    n = start_position + target
    while n > len(targets):
        n = n - len(targets)
    return n


def calc_left_position(star_position, target):
    # Left
    n = star_position - target
    while n < 0:
        n = len(targets) + n
    return n


while True:
    command = input().split('@')
    if command[0] == 'Game over':
        break

    if command[0] == 'Shoot Left':
        start, length = command[1:]
        start = int(start)
        length = int(length)

        if start in range(0, len(targets)):
            target = calc_left_position(start, length)

            if 0 <= targets[target] < 5:
                points += targets[target]
                targets[target] = 0
            elif targets[target] >= 5:
                points += 5
                targets[target] -= 5

    elif command[0] == 'Shoot Right':
        start, length = command[1:]
        start = int(start)
        length = int(length)

        if start in range(0, len(targets)):
            target = calc_rigth_position(start, length)

            if 0 <= targets[target] < 5:
                points += targets[target]
                targets[target] = 0
            elif targets[target] >= 5:
                points += 5
                targets[target] -= 5

    elif command[0] == 'Reverse':
        targets = targets[::-1]


print(" - ".join(str(x) for x in targets))
print(f'Iskren finished the archery tournament with {points} points!')