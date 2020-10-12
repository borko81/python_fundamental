'''
You will receive an initial list with groceries separated by "!".
After that you will be receiving 4 types of commands, until you receive "Go Shopping!"
    • Urgent {item} - add the item at the start of the list.  If the item already exists, skip this command.
    • Unnecessary {item} - remove the item with the given name, only if it exists in the list. Otherwise skip this
     command.
    • Correct {oldItem} {newItem} – if the item with the given old name exists, change its name with the new one.
     If it doesn't exist, skip this command.
    • Rearrange {item} - if the grocery exists in the list, remove it from its current position and add it at the
     end of the list.
'''

shoping_list = input().split('!')


def urgent(shoping_list, item):
    if item not in shoping_list:
        shoping_list.insert(0, item)


def unnecessary(shoping_list, item):
    if item in shoping_list:
        shoping_list.remove(item)


def correct(shoping_list, old_item, new_item):
    if old_item in shoping_list:
        shoping_list[shoping_list.index(old_item)] = new_item


def rearrange(shoping_list, item):
    if item in shoping_list:
        temp = shoping_list.pop(shoping_list.index(item))
        shoping_list.append(temp)


while True:
    command = input()
    if command == 'Go Shopping!':
        break

    elif command.startswith('Urgent'):
        command = command.split()
        urgent(shoping_list, command[1])

    elif command.startswith('Unnecessary'):
        command = command.split()
        unnecessary(shoping_list, command[1])

    elif command.startswith('Correct'):
        command = command.split()
        correct(shoping_list, command[1], command[2])

    elif command.startswith('Rearrange'):
        command = command.split()
        rearrange(shoping_list, command[1])


print(", ".join(shoping_list))