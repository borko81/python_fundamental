# 01. Valid Usernames
# line = input().split(', ')
#
# for l in line:
#     r = True
#     if len(l) < 3 or len(l) > 16:
#         r = False
#     else:
#         for i in l:
#             if not i.isalpha() and not i.isdigit() and i != '-' and i != '_':
#                 r = False
#                 break
#     if r is True:
#         print(l)

# 02. Character Multiplier
# line = input().split(' ')
# word_a = line[0]
# word_b = line[1]
# total = 0
#
# if len(word_a) == len(word_b):
#     for pos, a in enumerate(word_a):
#         total += ord(word_a[pos]) * ord(word_b[pos])
# elif len(word_a) < len(word_b):
#     for pos, a in enumerate(word_a):
#         total += ord(word_a[pos]) * ord(word_b[pos])
#     total += sum(ord(i) for i in word_b[len(word_a):])
# else:
#     for pos, a in enumerate(word_b):
#         total += ord(word_a[pos]) * ord(word_b[pos])
#     total += sum(ord(i) for i in word_a[len(word_b):])
#
#
# print(total)

# 03. Extract File

# path = input().split("\\")
# name, extension = path[-1].split('.')
# print(f'File name: {name}')
# print(f'File extension: {extension}')

# 04. Caesar Cipher
# word = input()
# result = ''
# for i in word:
#     result += chr(ord(i) + 3)
#
# print(result)

# 05. Emoticon Finder
# text = input()
#
# for pos, c in enumerate(text):
#     if c == ':' and text[pos+1] != ' ':
#         print(c + text[pos+1])

# 06. Replace Repeating Chars
# line = list(input())
#
# for i, c in enumerate(line, start=1):
#     for z in line[i:]:
#         if line[i] == line[i - 1]:
#             line.pop(i - 1)
#
# print("".join(line))

# 07. String Explosion
# line = input()
# power = 0
#
# for i in range(len(line)):
#     c = line[i]
#     if c == '>':
#         if line[i + 1].isdigit():
#             power += int(line[i + 1])
#     elif power > 0:
#         line = line[:i] + '0' + line[i + 1:]
#         power -= 1
#
# print(line.replace('0', ''))

# Letters change numbers
# total_score = 0
#
# def get_letter_post(letter):
#     num = 96
#     if letter.isupper():
#         num = 64
#
#     return ord(letter) - num
#
#
# def check_last(last_char, total):
#     if last_char.isupper():
#         total -= get_letter_post(last_char)
#         return total
#
#     elif last_char.islower():
#         total += get_letter_post(last_char)
#         return total
#
#
# words = input().split()
#
#
# for word in words:
#     total = 0
#     first_char = word[0]
#     last_char = word[-1]
#     t = int(word[1:-1])
#
#     if first_char.isupper():
#         total += t / get_letter_post(first_char)
#
#     else:
#         total += t * get_letter_post(first_char)
#
#     total_score += check_last(last_char, total)
#
# print(f'{total_score:.2f}')

# 09. Rage Quit
# line = input().upper()
#
#
# unique_symbol = set()
# return_string = ''
# text = ''
#
# for i in range(len(line)):
#     c = line[i]
#     if c not in ['1','2','3','4','5','6','7','8','9','0']:
#         text += c
#         unique_symbol.add(c)
#     elif c.isdigit():
#         dig = ''
#         while i < len(line) and line[i].isdigit():
#             dig += line[i]
#             i += 1
#         return_string += text * int(dig)
#         text = ''
#
#
# print(f'Unique symbols used: {len(unique_symbol)}')
# print(return_string)
#
# for _ in sorted(unique_symbol):
#     print(_)

# solve without zero *
# line = input().upper()
# unique_symbol = set()
# return_string = ''
# text = ''
#
# for i in range(len(line)):
#     c = line[i]
#     if c not in ['1','2','3','4','5','6','7','8','9','0']:
#         text += c
#     elif c.isdigit():
#         dig = ''
#         while i < len(line) and line[i].isdigit():
#             dig += line[i]
#             i += 1
#         return_string += text * int(dig)
#         text = ''
#
#
# print(f'Unique symbols used: {len(set(return_string))}')
# print(return_string)



# import re
#
# string = input().upper()
# result = []
# unique_chars = set()
# matches = re.finditer(r"(\D+)(\d+)", string)
# for match in matches:
#     num = int(match.group(2))
#     text = match.group(1)
#     if num == 0:
#         continue
#     for i in range(num):
#         result.append(text)
#     for char in text:
#         unique_chars.add(char)
#
# print(f"Unique symbols used: {len(set(unique_chars))}\n{''.join(result)}")
# for _ in sorted(set(unique_chars)):
#     print(_)

# 10. Winning Ticket
ticket = input().split(', ')
valid = '@#$^'


def max_repeating(str, search):
    """Търси за последователни символи"""

    l = len(str)
    count = 0

    for i in range(l):
        cur_count = 1

        for j in range(i + 1, l):

            if str[i] == str[j] == search:
                cur_count += 1
            else:
                break

        if cur_count > count:
            count = cur_count
    return count


for t in ticket:
    t = t.strip()
    ok = False
    Jack = False
    if len(t) != 20:
        print(f'invalid ticket')
    else:
        middle = len(t) // 2
        first = t[:middle]
        second = t[middle:]

        for v in valid:
            if t.count(v) == 20:
                Jack = True
                print(f'ticket "{t}" - {10}{v} Jackpot!')
                break

            f = max_repeating(first, v)
            s = max_repeating(second, v)

            if 6 <= f <= 10 and 6 <= s <= 10:
                ok = True
                print(f'ticket "{t}" - {min(f, s)}{v}')

        if ok is False and Jack is False:
            print(f'ticket "{t}" - no match')
























































