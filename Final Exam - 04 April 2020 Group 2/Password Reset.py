password = input()

while True:
    command = input()

    if command == 'Done':
        print(f"Your password is: {password}")
        break

    command = command.split()

    if command[0] == 'TakeOdd':
        new_string_password = ''
        for pos, char in enumerate(password):
            if pos & 1:
                new_string_password += char
        password = new_string_password
        print(password)

    elif command[0] == 'Cut':
        index, length = map(int, command[1:])
        new_string_password = password[:index] + password[index + length:]
        password = new_string_password
        print(password)

    elif command[0] == 'Substitute':
        substring, new_string = command[1:]
        if substring in password:
            password = password.replace(substring, new_string)
            print(password)
        else:
            print("Nothing to replace!")

"""
Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string and afterwards, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:
    • TakeOdd
        ◦  Takes only the characters at odd indices and concatenates them together to
obtain the new raw password and then prints it.
    • Cut {index} {length}
        ◦ Gets the substring with the given length starting from the given index from the password and removes its first occurrence of it, then prints the password on the console.
        ◦ The given index and length will always be valid.
    • Substitute {substring} {substitute}
        ◦ If the raw password contains the given substring, replaces all of its 
occurrences with the substitute text given and prints the result.
        ◦ If it doesn’t, prints "Nothing to replace!"
Input
    • You will be receiving strings until the "Done" command is given.
Output
    • After the "Done" command is received, print:
        ◦ "Your password is: {password}"
Constraints
    • The indexes from the "Cut {index} {length}" command will always be valid.
"""

# Input
"""
Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr 
TakeOdd
Cut 15 3
Substitute :: -
Substitute | ^
Done
"""
