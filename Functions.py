# 01. Grades
# grade = float(input())
#
#
# def solve(grade):
#     if 2.00 <= grade <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade <= 4.49:
#         return 'Good'
#     elif 4.5 <= grade <= 5.49:
#         return 'Very Good'
#     elif 5.5 <= grade <= 6.00:
#         return 'Excellent'
#
# print(solve(grade))

# 02. Calculations
# operator = input()
# a = int(input())
# b = int(input())
#
# def solve(operator, a, b):
#     if operator == 'multiply':
#         return a * b
#     elif operator == 'divide':
#         return  a // b
#     elif operator == 'add':
#         return a + b
#     elif operator == 'subtract':
#         return  a - b
#
# print(solve(operator, a, b))

# 03. Repeat String
# word = input()
# count = int(input())
#
#
# def solve(word, count):
#     return word * count
#
# print(solve(word, count))

# 04. Orders
# word = input()
# quantity = float(input())
#
#
# def solve(word, quantity):
#     if word == 'coffee':
#         return f'{quantity * 1.50:.2f}'
#     elif word == 'water':
#         return f'{quantity * 1:.2f}'
#     elif word == 'coke':
#         return f'{quantity * 1.4:.2f}'
#     elif word == 'snacks':
#         return f'{quantity * 2:.2f}'
#
#
# print(solve(word, quantity))

# 05. Calculate Rectangle Area
# width = int(input())
# height = int(input())
#
#
# def solve(width, height):
#     return width * height
#
#
# print(solve(width, height))


# -----------------------Exercies ---------------------------------

# 01. Smallest of Three Numbers
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# def get_small(a, b, c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     else:
#         return c
#
#
# print(get_small(a, b, c))

# 02. Add and Subtract
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# def sum_numbers():
#     return a + b
#
#
# def subtract():
#     return sum_numbers() - c
#
#
# print(subtract())

# 03. Characters in Range
# a = input()
# b = input()
# int_a = ord(a)
# int_b = ord(b)
#
#
# def solve():
#     return " ".join([chr(i) for i in range(int_a + 1, int_b)])
#
#
# print(solve())

# 04. Odd and Even Sum
# number = int(input())
#
#
# def solve(number):
#     result = []
#     while number:
#         check = number
#         result.append(check % 10)
#         number //= 10
#     even = sum([i for i in result if i % 2 == 0])
#     odd = sum([i for i in result if i % 2 != 0])
#     return f'Odd sum = {odd}, Even sum = {even}'
#
#
# print(solve(number))

# 05. Palindrome Integers
# numbers = [int(i) for i in input().split(', ')]
#
#
# def check_palindrome_or_not(num):
#     if num == int("".join(reversed(str(num)))):
#         return True
#     return False
#
#
# for _ in numbers:
#     print(check_palindrome_or_not(_))

# 06. Password Validator
# password = input()
#
#
# def validate_password():
#     valid = False
#     dig = 0
#     w = 0
#     if 6 <= len(password) <= 10:
#         valid = True
#     else:
#         valid = False
#         print('Password must be between 6 and 10 characters')
#
#     for _ in password:
#         if _.isalpha() or _.isdigit():
#             if _.isdigit():
#                 dig += 1
#             elif _.isalpha():
#                 w += 1
#         else:
#             valid = False
#             print('Password must consist only of letters and digits')
#             break
#
#     if dig < 2:
#         print(f'Password must have at least 2 digits')
#
#     if valid == True and dig >= 2 and w > 1:
#         print('Password is valid')
#
#
# validate_password()

# 07. Perfetct Number
# number = int(input())
#
#
# def solve():
#     if number % 2 == 0:
#         s = 0
#         for _ in range(1, number//2 + 1):
#             if number % _ == 0:
#                 s += _
#         if s == number:
#             print('We have a perfect number!')
#         else:
#             print("It's not so perfect.")
#     else:
#         print("It's not so perfect.")
#
#
# solve()


# 08. Loading Bar
# n = int(input())
#
# def solve():
#     if n == 100:
#         print(f'{n}% Complete!')
#         print('[%%%%%%%%%%]')
#     else:
#         s = n // 10
#         g = 10 - s
#         print(f'{n}% [{"%"*s}{"."*g}]')
#         print(f'Still loading...')
#
# solve()

# 09. Factorial Division
# a = int(input())
# b = int(input())
#
#
# def factoriel(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact
#
#
# print(f'{(factoriel(a) / factoriel(b)):.2f}')

# 10. Array Manipulator
# import sys
#
#
# def exchange(numbers, i):
#     first_part = numbers[:i + 1]
#     second_part = numbers[i + 1:]
#     return second_part + first_part
#
#
# def max_even_index(numbers, even):
#     max_number_even = -sys.maxsize
#     max_number_even_index = -1
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == even and numbers[i] >= max_number_even:
#             max_number_even = numbers[i]
#             max_number_even_index = i
#
#     if max_number_even_index == -1:
#         return 'No matches'
#     else:
#         return max_number_even_index
#
#
# def min_even_index(numbers, even):
#     min_number_even = sys.maxsize
#     max_number_even_index = -1
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == even and numbers[i] <= min_number_even:
#             min_number_even = numbers[i]
#             max_number_even_index = i
#
#     if max_number_even_index == -1:
#         return 'No matches'
#     else:
#         return max_number_even_index
#
#
# def first(numbers, event, counter):
#     first_list_odd = []
#     count = 0
#     for number in numbers:
#         if count == counter:
#             break
#         if number % 2 == event:
#             first_list_odd.append(number)
#             count += 1
#
#     return first_list_odd
#
#
# def last(numbers, even, counter):
#     last_list_even = []
#     count = 0
#     for i in range(len(numbers) - 1, -1, -1):
#
#         if count == counter:
#             break
#
#         if numbers[i] % 2 == even:
#             last_list_even.append(numbers[i])
#             count += 1
#
#     return last_list_even[::-1]
#
#
# numbers_list = input().split(' ')
# numbers_list = [int(x) for x in numbers_list]
#
# command_input = input().split(' ')
# while command_input[0] != 'end':
#     command = command_input[0]
#
#     if command == 'exchange':
#         index = int(command_input[1])
#         if len(numbers_list) > index >= 0:
#             numbers_list = exchange(numbers_list, index)
#         else:
#             print('Invalid index')
#     elif command == 'max':
#         criteria = command_input[1]
#         res = max_even_index(numbers_list, 0 if criteria == "even" else 1)
#         print(res)
#     elif command == 'min':
#         criteria = command_input[1]
#         res = min_even_index(numbers_list, 0 if criteria == "even" else 1)
#         print(res)
#     elif command == 'first':
#         criteria = command_input[2]
#         index = int(command_input[1])
#         if len(numbers_list) >= index >= -1:
#             print(first(numbers_list, 0 if criteria == "even" else 1, index))
#         else:
#             print('Invalid count')
#     elif command == 'last':
#         criteria = command_input[2]
#         index = int(command_input[1])
#         if len(numbers_list) >= index >= -1:
#             print(last(numbers_list, 0 if criteria == "even" else 1, index))
#         else:
#             print('Invalid count')
#
#     command_input = input().split(' ')
#
# print(numbers_list)


# 01. Data Types
# choice = input()
# work = input()
#
#
# def choice_int(work):
#     print(int(work) * 2)
#
#
# def choice_real(work):
#     print(f'{(float(work) * 1.5):.2f}')
#
#
# def choice_string(work):
#     print(f"{'$'}{work}{'$'}")
#
#
# def solve():
#     if choice == 'int':
#         choice_int(work)
#     elif choice == 'real':
#         choice_real(work)
#     elif choice == 'string':
#         choice_string(work)
#
#
# solve()

# 02. Center Point
# import math
# x_1 = float(input())
# y_1 = float(input())
# x_2 = float(input())
# y_2 = float(input())
#
#
# def solve(x_1, y_1, x_2, y_2):
#     result_one = abs(math.sqrt(math.pow(x_1, 2) + math.pow(y_1, 2)))
#     result_tow = abs(math.sqrt(math.pow(x_2, 2) + math.pow(y_2, 2)))
#     if result_one < result_tow:
#         print(f'({int(x_1)}, {int(y_1)})')
#     else:
#         print(f'({int(x_2)}, {int(y_2)})')
#
#
# solve(x_1, y_1, x_2, y_2)

# 03. Longer Line
# import math
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x3 = float(input())
# y3 = float(input())
# x4 = float(input())
# y4 = float(input())
#
# def distance(x, y):
#     return math.sqrt(x ** 2 + y ** 2)
#
# def solve(x1, y1, x2, y2, x3, y3, x4, y4):
#     r1 = distance(x1, y1)
#     r2 = distance(x2, y2)
#     r3 = distance(x3, y3)
#     r4 = distance(x4, y4)
#
#     len12 = math.sqrt((x1 - x2) ** 2) + math.sqrt((y1 - y2) ** 2)
#     len34 = math.sqrt((x3 - x4) ** 2) + math.sqrt((y3 - y4) ** 2)
#
#     x1 = int(x1)
#     y1 = int(y1)
#     x2 = int(x2)
#     y2 = int(y2)
#     x3 = int(x3)
#     y3 = int(y3)
#     x4 = int(x4)
#     y4 = int(y4)
#
#     if len12 >= len34:
#         if r1 <= r2:
#             print(f'({x1}, {y1})({x2}, {y2})')
#         else:
#             print(f'({x2}, {y2})({x1}, {y1})')
#     else:
#         if r3 <= r4:
#             print(f'({x3}, {y3})({x4}, {y4})')
#         else:
#             print(f'({x4}, {y4})({x3}, {y3})')
#
#
# solve(x1, y1, x2, y2, x3, y3, x4, y4)

# 04. Tribonacci Sequence
# n = int(input())
#
# def solve(n):
#     result = []
#     gen = 1
#     while len(result) < n:
#         result.append(gen)
#         gen = sum(result[-3:])
#
#     print(" ".join(str(i) for i in result))
#
#
# solve(n)

# 05. Multiplication Sign
num1 = float(input())
num2 = float(input())
num3 = float(input())


# def solve():
#     if num1 == 0 or num2 == 0 or num3 == 0:
#         print('zero')
#     else:
#         if num1 < 0 or num2 < 0 or num3 < 0:
#             print('negative')
#         else:
#             print('positive')

def solve2():
    r = num1 * num2 * num3
    if r == 0:
        print('zero')
    elif r > 0:
        print('positive')
    else:
        print('negative')

solve2()


























































