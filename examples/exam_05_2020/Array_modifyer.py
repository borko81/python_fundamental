array = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'end':
        break

    if command.startswith('swap'):
        _, f_pos, l_pos = command.split()
        f_pos = int(f_pos)
        l_pos = int(l_pos)
        #array[array.index(f_pos)],  array[array.index(l_pos)] = array[array.index(l_pos)], array[array.index(f_pos)]
        array[f_pos], array[l_pos] = array[l_pos], array[f_pos]

    elif command.startswith('multiply'):
        _, f_pos, l_pos = command.split()
        f_pos = int(f_pos)
        l_pos = int(l_pos)
        array[f_pos] *= array[l_pos]

    elif command.startswith('decrease'):
        array = [x - 1 for x in array]


print(", ".join(str(x) for x in array))