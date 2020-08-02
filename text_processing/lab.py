# 01. Reverse Strings
# line = input()
#
# while line != 'end':
#     print(f'{line} = {"".join(reversed(line))}')
#     line = input()

# 02. Repeat Strings
# def solve(line):
#     for word in line.split(' '):
#         n = len(word)
#         print(word * n, end='')
#
# solve(input())

# 03. Substring
# search = input()
# word = input()
#
# while search in word:
#     word = word.replace(search, '')
#
# print(word)

# 04. Text Filter
# ban_list = input().split(', ')
# text = input()
#
# for word in ban_list:
#     while word in text:
#         text = text.replace(word, '*' * len(word))
#
# print(text)

# 05. Digits, Letters and Other
single_string = input()
digit = ''
letter = ''
whitespace = ''

for w in single_string:
    if w.isdigit():
        digit += w
    elif w.isalpha():
        letter += w
    else:
        whitespace += w

print(digit)
print(letter)
print(whitespace)

































