'''
First, you will receive a skill that needs the deciphered.
Next, you will be receiving commands split by a single space until you get the "For Azeroth" command. There are 5 possible commands:

    • "GladiatorStance"
        ◦ Replace all letters with upper case and print the result.
    • "DefensiveStance"
        ◦ Replace all letters with lower case and print the result.
    • "Dispel {index} {letter}"
        ◦ Replace the letter at the index with the given one and print "Success!"
        ◦ If the index is invalid, print: "Dispel too weak."
    • "Target Change {substring} {second substring}"
        ◦ Replace the first substring with the second and print the result.
    • "Target Remove {substring}"
        ◦ Remove the substring from the string and print the result.

If the input command is not in the list, print "Command doesn't exist!"
'''


skill = input()


def gladiatorStance(text):
    text = text.upper()
    print(text)
    return text


def defensiveStance(text):
    text = text.lower()
    print(text)
    return text


def target_change(skill, substring, secodnsubstring):
    #for pos_one, e in enumerate(substring):
    skill = skill.replace(substring, secodnsubstring)
    print(skill)
    return skill


def dispel(string, index, letter):
    if index in range(len(string)):
        string = list(string)
        string[index] = letter
        print('Success!')
    else:
        print('Dispel too weak.')
    return "".join(string)


def target_remove(string, substr):
    string = string.replace(substr, '')
    print(string)
    return string


while True:
    command = input()
    if command == 'For Azeroth':
        break

    command = command.split()
    if command[0] == 'GladiatorStance':
        skill = gladiatorStance(skill)

    elif command[0] == 'DefensiveStance':
        skill = defensiveStance(skill)

    elif command[0] == 'Dispel':
        _, index, letter = command
        index = int(index)
        skill = dispel(skill, index, letter)

    elif command[0] + ' ' + command[1] == 'Target Change':
        substring, secodnsubstring = command[2], command[-1]
        skill = target_change(skill, substring, secodnsubstring)

    elif command[0] + ' ' + command[1] == 'Target Remove':
        substr = command[-1]
        skill = target_remove(skill, substr)

    else:
        print('Command doesn\'t exist!')
