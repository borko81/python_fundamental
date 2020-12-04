raw_activation_key = input()


def generate(raw_string, substr):
    if substr not in raw_string:
        print("Substring not found!")
    else:
        print(f"{raw_activation_key} contains {substr}")


def flip(raw_string, up_low, start, end):
    middle_index = raw_string[start: end]
    if up_low == 'Upper':
        raw_string = raw_string[:start] + middle_index.upper() + raw_string[end:]
    else:
        raw_string = raw_string[:start] + middle_index.lower() + raw_string[end:]
    print(raw_string)
    return raw_string


def slice(raw_string, start, end):
    middle_index = raw_string[start: end]
    raw_string = raw_string.replace(middle_index, '', 1)
    print(raw_string)
    return raw_string


while True:
    command = input()
    if command == 'Generate':
        break

    command = command.split('>>>')

    if command[0] == 'Contains':
        comamnd, substring, *arg = command
        generate(raw_activation_key, substring)

    elif command[0] == 'Flip':
        command, up_or_low, start, end, *arg = command
        start = int(start)
        end = int(end)
        raw_activation_key = flip(raw_activation_key, up_or_low, start, end)

    elif command[0] == 'Slice':
        command, start, end, *arg = command
        start = int(start)
        end = int(end)
        raw_activation_key = slice(raw_activation_key, start, end)

print(f"Your activation key is: {raw_activation_key}")

"""
The first line of the input will be your raw activation key. It will consist of letters and numbers only. 
After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
    • Contains>>>{substring} – checks if the raw activation key contains the given substring.
        ◦ If it does prints: "{raw activation key} contains {substring}".
        ◦ If not, prints: "Substring not found!"
    • Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}
        ◦ Changes the substring between the given indices (the end index is exclusive) to upper or lower case. 
        ◦ All given indexes will be valid.
        ◦ Prints the activation key.
    • Slice>>>{startIndex}>>>{endIndex}
        ◦ Deletes the characters between the start and end indices (end index is exclusive).
        ◦ Both indices will be valid.
        ◦ Prints the activation key.
"""
