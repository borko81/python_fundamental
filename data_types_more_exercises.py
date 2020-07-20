# 01. Biggest of 3 Numbers
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# 02. Exchange Integers
# a = int(input())
# b = int(input())
#
# print('Before:')
# print(f'a = {a}')
# print(f'b = {b}')
# a, b = b, a
# print('After:')
# print(f'a = {a}')
# print(f'b = {b}')

#03. Prime Number Checker
# n = int(input())
# result = True
# for i in range(2, n + 1 // 2):
#     if n % i == 0:
#         result = False
#         break
#
# print(result)

# 04. Decrypting Messages
# key = int(input())
# lines = int(input())
# message = ''
#
# for i in range(lines):
#     char = input()
#     message += chr(key + ord(char))
#
# print(message)

# 05. Balanced Brackets
# n = int(input())
# get_result = 0
#
# for i in range(n):
#     if get_result == 2:
#         break
#     l = input()
#     if l == '(':
#         get_result += 1
#     elif l == ')':
#         get_result -= 1
#
# if get_result == 0:
#     print('BALANCED')
# else:
#     print('UNBALANCED')


















