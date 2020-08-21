'''
Create a program that follows instructions in order to fulfil a quest. First, you will receive a collection of numbers – each representing a painting number. After that, you are going to be receiving instructions, until the "END" command is given.
    • Change {paintingNumber} {changedNumber} – find the painting with the first number in the collection (if it exists) and change its number with the second number – {changedNumber}.
    • Hide {paintingNumber} – find the painting with this value and if it exists and hide it (remove it).
    • Switch {paintingNumber} {paintingNumber2} – find the given paintings in the collections if they exist and switch their places.
    • Insert {place} {paintingNumber} – insert the painting (paintingNumber) on the next place after the given one, if it exists.
    • Reverse – you must reverse the order of the paintings.
Once you complete the instructions, print the numbers of the paintings on a single line, split by a space.
'''


enter_numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'END':
        break

    if command.startswith('Insert'):
        com, position, item = command.split()
        if int(position) + 1 <= len(enter_numbers):
            enter_numbers.insert(int(position) + 1, int(item))

    elif command.startswith('Change'):
        com, search, changeitem = command.split()

        search = int(search)
        changeitem = int(changeitem)
        try:
            index_item = enter_numbers.index(search)
            enter_numbers[index_item] = changeitem
        except:
            pass

    elif command.startswith('Hide'):
        com, searchitem = command.split()
        searchitem = int(searchitem)
        try:
            enter_numbers.pop(enter_numbers.index(searchitem))
        except:
            pass

    elif command.startswith('Switch'):
        com, first_number, second_number = command.split()
        first_number = int(first_number)
        second_number = int(second_number)
        try:
            index_one = enter_numbers.index(first_number)
            index_two = enter_numbers.index(second_number)
            enter_numbers[index_one], enter_numbers[index_two] = enter_numbers[index_two], enter_numbers[index_one]
        except:
            pass

    elif command.startswith('Reverse'):
        enter_numbers = enter_numbers[::-1]


print(" ".join(str(x) for x in enter_numbers))
