'''Your task is to take every word and insert it into the dictionary with its definition. A word may have one or more
definitions. You will receive all the words and definitions, separated by " | ", and each word and its definition will
be separated by ": ".
After this you will have to check the words you have in the dictionary. Now you will receive only words, again
separated by" | ". For each word you get you will have to print it and all of its definitions, ordered by length of
the definition in descending order(if it exists in the dictionary) in the following format:
"{word}:"
" –{definition1}"
" –{definition2}"
" –{definition3}"
. . .
In the end, you will receive one more command, which will be either "End" or "List". If the command is "End",
you should break the program. If the command is "List", you should print all of the words, ordered alphabetically,
separated by space (" ").
'''

result = {}


first_line = input()

target_l = first_line.split(' | ')
for get in target_l:
    try:
        word, definition = get.split(': ')
        if word not in result:
            result[word] = [definition]
        else:
            result[word].append(definition)
    except:
        pass

second_line = input().split(' | ')

l = input()
if l == 'End':
    for key, val in sorted(result.items()):
        if key in second_line:
            print(f'{key}')
            for v in sorted(val, key=lambda x: -len(x)):
                print(f' -{v}')

elif l == 'List':
    print(" ".join(sorted(result.keys())))

