message = list(input())

while True:

    command = input()
    if command == 'Reveal':
        message = "".join(message)
        print(f"You have a new text message: {message}")
        break

    command = command.split(':|:')

    if command[0] == 'InsertSpace':
        index = int(command[1])
        message.insert(index, ' ')
        print("".join(message))

    elif command[0] == 'Reverse':
        substring = command[1]
        message = "".join(message)
        if substring not in message:
            print("error")
            message = list(message)
        else:
            message = message.replace(substring, '', 1)
            substring = substring[::-1]
            message += substring
            message = list(message)
            print("".join(message))

    elif command[0] == 'ChangeAll':
        substring, replacement = command[1:]
        message = "".join(message)
        if substring in message:
            message = message.replace(substring, replacement)
        else:
            print("error")

        message = list(message)
        print("".join(message))

"""
On the first line of the input you will receive the concealed message. After that, until the "Reveal" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message in order to interpret it and reveal its true content. There are several types of instructions, split by ":|:"
    • InsertSpace:|:{index}
        ◦ Inserts a single empty space at the given index. The given index will always be valid.
    • Reverse:|:{substring}
        ◦ If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
        ◦ If not, print "error". 
        ◦ This operation should replace only the first occurrence of the given substring if there are more than one such occurrences.
    • ChangeAll:|:{substring}:|:{replacement} 
        ◦ Changes all occurrences of the given substring with the replacement text.
"""

# INPUT
"""
heVVodar!gniV
ChangeAll:|:V:|:l
Reverse:|:!gnil
InsertSpace:|:5
Reveal
"""
