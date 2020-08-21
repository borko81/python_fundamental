'''
Create a program that follows given instructions. You will receive a collection of words on a single line, split by a
single space. They are not what they are supposed to be, so you have to follow the instructions in order to find the real
message. You will be receiving commands. Here are the possible ones:
    • Delete {index} – removes the word after the given index if it is valid.
    • Swap {word1} {word2} – find the given words in the collections if they exist and swap their places.
    • Put {word} {index} – add a word at the previous place {index} before the
given one, if it is valid. Note: putting at the last index simply appends the word to the end of the list.
    • Sort – you must sort the words in descending order.
    • Replace {word1} {word2} – find the second word {word2} in the collection (if it exists) and replace it with
     the first word – {word1}.
Follow them until you receive the "Stop" command. After you have successfully followed the instructions,
you must print the words on a single line, split by a space.
'''

text = input().split()

while True:
    command = input()
    if command == 'Stop':
        break

    if command.startswith('Delete'):
        index = command.split()[1]
        index = int(index) + 1
        if index < len(text):
            text.pop(index)

    elif command.startswith('Swap'):
        _, start, end = command.split()
        try:
            start_get = text.index(start)
            end_get = text.index(end)
            text[start_get], text[end_get] = text[end_get], text[start_get]
        except:
            pass

    elif command.startswith('Put'):
        _, word, index = command.split()
        index = int(index) - 1
        if index >= 0 and index <= len(text):
            text.insert(index, word)

    elif command.startswith('Sort'):
        text = sorted(text, reverse=True)

    elif command.startswith('Replace'):
        _, first, second = command.split()
        try:
            index = text.index(second)
            text[index] = first
        except:
            pass


print(" ".join(text))