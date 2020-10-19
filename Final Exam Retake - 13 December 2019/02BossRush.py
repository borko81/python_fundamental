'''
Create a program that checks if inputs are valid and decrypt it. On the first line you will receive a number that indicates how many inputs you will receive on the next lines.

You will read lines with a boss name and title and you should check if they are valid, considering the following rules:
    • Boss - the name should be in upper case letters, should be minimum four letters long and should be surrounded by "|"
    • Title - contains exactly 2 words and they contain only alphabetical letters and 1 whitespace between them. The title should be surrounded by "#"
    • The name and title should be split by a single ":"
Example for a valid input:  |GEORGI|:#Lead architect#
If the input is valid. Print in the following format:
"{boss name}, The {title}
>> Strength: {length of the name}
>> Armour: {length of the title}"
'''

import re

number_input = int(input())

for _ in range(number_input):
    command = input()
    pattern = re.compile(r'\|([A-Z]+)\|:#([a-zA-Z]+\s[a-zA-Z]+)#')
    test = pattern.match(command)
    if test:
        print(f"{test.group(1)}, The {test.group(2)}")
        print(f">> Strength: {len(test.group(1))}")
        print(f">> Armour: {len(test.group(2))}")
    else:
        print('Access denied!')