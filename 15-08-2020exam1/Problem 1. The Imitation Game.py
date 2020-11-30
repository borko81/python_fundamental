message = input()

# zzHe

while True:
    command = input()

    if command == 'Decode':
        print(f"The decrypted message is: {message}")
        break

    command = command.split('|')
    
    if command[0] == 'Move':
        n = int(command[1])
        message = list(message)
        message = message[n:] + message[:n]
        message = "".join(message)

    elif command[0] == 'Insert':
        search_index = int(command[1])
        value = command[2]
        message = list(message)
        message.insert(search_index, value)
        message = "".join(message)

    elif command[0] == 'ChangeAll':
        char = command[1]
        char_to_replace = command[2]
        message = message.replace(char, char_to_replace)
