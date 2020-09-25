elements = input().split()

moves = 0

while True:
    line = input()
    if line == 'end':
        break

    f, l = map(int, line.split())

    moves += 1

    if f < 0 or f >= len(elements) or l < 0 or l >= len(elements) or f == l:
        print('Invalid input! Adding additional elements to the board')
        elements.insert(len(elements) // 2, f'-{moves}a')
        elements.insert(len(elements) // 2, f'-{moves}a')

    elif elements[f] == elements[l]:
        print(f'Congrats! You have found matching elements - {elements[f]}!')
        if f > l :
            del elements[f]
            del elements[l]
        else:
            del elements[l]
            del elements[f]

        if len(elements) == 0:
            print(f'You have won in {moves} turns!')
            break

    elif elements[f] != elements[l]:
        print('Try again!')


if len(elements) > 0:
    print('Sorry you lose :(')
    print(" ".join(x for x in elements))