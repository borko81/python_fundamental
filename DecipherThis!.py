import re
# message = input().split()
message = '82yade 115te 103o'.split()


def change_f_letter(word):
    s = []
    for i in word:
        if i.isdigit():
            s.append(i)
    word = chr(int("".join(s))) + word[len(s):]
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    return "".join(word)


message = [change_f_letter(i) for i in message]

print(" ".join(message))