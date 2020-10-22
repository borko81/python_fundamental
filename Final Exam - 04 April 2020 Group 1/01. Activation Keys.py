activation_key = input()

command = input()

while command != 'Generate':
    command = command.split(">>>")

    if command[0] == 'Contains':
        search = command[1]
        if len(activation_key) > 0 and search in activation_key:
            print(f'{activation_key} contains {search}')
        else:
            print('Substring not found!')

    elif command[0] == 'Flip':
        action = command[1]
        startindex, endindex = map(int, command[2:])

        if startindex in range(len(activation_key)) and endindex in range(len(activation_key)) and startindex <= endindex:
            temp = activation_key[startindex:endindex]
            if action == 'Upper' and len(activation_key) > 0:
                activation_key = activation_key[:startindex] + temp.upper() + activation_key[endindex:]
            elif action == 'Lower' and len(activation_key) > 0:
                activation_key = activation_key[:startindex] + temp.lower() + activation_key[endindex:]
            print(activation_key)

    elif command[0] == 'Slice':
        startindex, endindex = map(int, command[1:])
        if startindex in range(len(activation_key)) and endindex in range(len(activation_key)) and startindex <= endindex:
            if len(activation_key) > 0:
                activation_key = activation_key[:startindex] + activation_key[endindex:]
                print(activation_key)

    command = input()

print(f'Your activation key is: {activation_key}')