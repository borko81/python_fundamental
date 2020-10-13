n = int(input())

train = [[0] for _ in range(n)]

while True:
    command = input().split()
    if command[0] == 'End':
        break

    elif command[0] == 'add':
        _, people = command
        people = int(people)
        train[-1][0] += people

    elif command[0] == 'insert':
        _, index, people = command
        index, people = int(command[1]), int(command[2])
        if index in range(n):
            train[index][0] += people

    elif command[0] == 'leave':
        _, index, people = command
        index, people = int(command[1]), int(command[2])
        if index in range(n):
            train[index][0] -= people


print([x for z in train for x in z])