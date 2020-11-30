stops = list(input())

while True:
    command = input()
    if command == 'Travel':
        stops = "".join(stops)
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    command = command.split(':')

    if command[0] == 'Add Stop':
        index, string = command[1:]
        index = int(index)
        if 0 <= index < len(stops):
            string = list(string)
            stops = stops[:index] + string + stops[index:]
        print("".join(stops))

    elif command[0] == 'Remove Stop':
        start, stop = map(int, command[1:])
        if start in range(len(stops)) and stop in range(len(stops)):
            stops = stops[:start] + stops[stop + 1:]
        print("".join(stops))

    elif command[0] == 'Switch':
        old, new = command[1:]
        stops = "".join(stops)
        if old in stops:
            stops = list(stops.replace(old, new))
        print("".join(stops))

"""
On the first line you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
    • Add Stop:{index}:{string} – insert the given string at that index only if the index is valid
    • Remove Stop:{start_index}:{end_index} – remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
    • Switch:{old_string}:{new_string} – if the old string is in the initial string, replace it with the new one. (all occurrences)
Note: After each command print the current state of the string
After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"""

"""INPUT
Hawai::Cyprys-Greece
Add Stop:7:Rome
Remove Stop:11:16
Switch:Hawai:Bulgaria
Travel
"""
