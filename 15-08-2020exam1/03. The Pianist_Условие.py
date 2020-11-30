number_of_pieces = int(input())

# {piece}|{composer}|{key}

result = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if piece not in result:
        result[piece] = [composer, key]
    else:
        result[piece].append([composer, key])

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split('|')
    if command[0] == 'Add':
        piece, composer, key = command[1:]
        if piece in result:
            print(f"{piece} is already in the collection!")
        else:
            result[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == 'Remove':
        piece = command[1]
        if piece not in result:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del result[piece]
            print(f"Successfully removed {piece}!")

    elif command[0] == 'ChangeKey':
        piece, new_key = command[1:]
        if piece not in result:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            result[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for key, value in sorted(result.items(), key=lambda x: (x[0], x[1][0])):
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")

"""
On the first line of the standard input you will receive an integer n – the number of pieces that you will initially have. On the next n lines the pieces themselves will follow with their composer and key, separated by "|" in the following format:
{piece}|{composer}|{key}
Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
    • Add|{piece}|{composer}|{key} 
        ◦ You need to add the given piece with the information about it to the other pieces
        ◦ If the piece is already in the collection, print:
"{piece} is already in the collection!"
        ◦ If the piece is not in the collection, print: 
"{piece} by {composer} in {key} added to the collection!"
    • Remove|{piece}
        ◦ If the piece is in the collection, remove it and print:
"Successfully removed {piece}!"
        ◦ If the piece is not in the collection, print:
"Invalid operation! {piece} does not exist in the collection."
    • ChangeKey|{piece}|{new key}
        ◦ If the piece is in the collection, change its key with the given one and print:
"Changed the key of {piece} to {new key}!"
        ◦ If the piece is not in the collection, print:
"Invalid operation! {piece} does not exist in the collection."
Upon receiving the "Stop" command you need to print all pieces in your collection, sorted by their name and by the name of their composer in alphabetical order, in the following format:
"{Piece} -> Composer: {composer}, Key: {key}"""
