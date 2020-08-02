# 01. Extract Person Information
# number_of_line = int(input())
#
# for _ in range(number_of_line):
#     info = input()
#     name_f_char = info.index('@')
#     name_l_char = info.index('|')
#     age_f_char = info.index('#')
#     age_l_char = info.index('*')
#     print(f"{info[name_f_char + 1:name_l_char]} is {info[age_f_char + 1: age_l_char]} years old.")

# 02. Ascii Sumator
# f_char = ord(input())
# l_char = ord(input())
# line = input()
# min, max = min(f_char, l_char), max(f_char, l_char)
#
# total = 0
#
# for i in line:
#     c = ord(i)
#     if min < c < max:
#         total += c
#
# print(total)

# 03. Treasure Finder
# import copy
# key_me = [int(i) for i in input().split()]
#
# while True:
#     line = input()
#     key = copy.copy(key_me)
#     total = ''
#     if line == 'find':
#         break
#
#     for i in line:
#         at_me = key.pop(0)
#         total += chr(ord(i) - at_me)
#         key.append(at_me)
#
#     try:
#         first_found = total.index('&')
#         second_found = total.index('&', first_found + 1)
#         f_fount = total.index('<')
#         l_found = total.index('>')
#     except:
#         pass
#     else:
#         name = total[first_found + 1: second_found]
#         coordinate = total[f_fount + 1: l_found]
#         print(f'Found {name} at {coordinate}')

# 04. Morse Code Translator
# code_dict =  {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
#      '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
#      '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
#      '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
#      '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
#      '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
#      '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
#      '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
#      '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
#      '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
#      '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
#      }
# line = input()
# def decode(line):
#     decrypt_message = []
#     for l in line.split():
#         if l != '|':
#             decrypt_message.append(code_dict.get(l))
#         else:
#             decrypt_message.append(l)
#     decrypt_message = [i for i in decrypt_message if not i.isdigit()]
#     decrypt_message = [i.replace('|', ' ') for i in decrypt_message]
#     return decrypt_message
#
# print("".join(decode(line)))

# 05. HTML
# title = input()
# content_article = input()
#
# html = []
# html.append(f'<h1>\n\t{title}\n</h1>')
# html.append(f'<article>\n\t{content_article}\n</article>')
#
# while True:
#     comments = input()
#     if comments == 'end of comments':
#         break
#     else:
#         html.append(f'<div>\n\t{comments}\n</div>')
#
# for l in html:
#     print(l)




























