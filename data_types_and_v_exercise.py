# 01. Integer Operations
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# result = ((a + b) // c) * d
# print(int(result))

# 02. Chars to String
# a = input()
# b = input()
# c = input()
# print(f'{a}{b}{c}')

#03. Elevator
# number_of_people = int(input())
# capacity = int(input())
#
# check = number_of_people / capacity
# if check != number_of_people // capacity:
#     print(int(check) + 1)
# else:
#     print(int(check))

# 04. Sum of Chars
# n = int(input())
# total = 0
#
# while n > 0:
#     total += ord(input())
#     n -= 1
#
# print(f'The sum equals: {total}')

# 05. Print Part of the ASCII Table
# f_index = int(input())
# l_index = int(input())
#
# for _ in range(f_index, l_index + 1):
#     print(chr(_), end=' ')

# 06. Triples of Latin Letters
# n = int(input())
# START_POSITION = 97
#
# for a in range(START_POSITION, START_POSITION + n):
#     for b in range(START_POSITION, START_POSITION + n):
#         for c in range(START_POSITION, START_POSITION + n):
#             print(f'{chr(a)}{chr(b)}{chr(c)}')

# 07. Water Overflow
# WATER_CAPACITY = 255
#
# n = int(input())
# total_water_get = 0
#
# while n > 0:
#     water = int(input())
#     if total_water_get + water > WATER_CAPACITY:
#         print('Insufficient capacity!')
#     else:
#         total_water_get += water
#     n -= 1
#
# print(total_water_get)

# 08. Party Profit
# party_size = int(input())
# days = int(input())
# coins = 0
#
# for day in range(1, days + 1):
#     if day % 10 == 0:
#         party_size -= 2
#     if day % 15 == 0:
#         party_size += 5
#         coins -= party_size * 2
#
#     coins += 50 - (party_size * 2)
#
#     if day % 3 == 0:
#         coins -= party_size * 3
#     if day % 5 == 0:
#         coins += party_size * 20
#
# print(f'{party_size} companions received {(coins//party_size)} coins each.')

# 09. Snowballs
# n = int(input())
#
# m_value = -999
# result = ''
#
# for _ in range(1, n + 1):
#     snowballSnow = int(input())
#     snowballTime = int(input())
#     snowballQuality = int(input())
#     snowballValue = (snowballSnow // snowballTime) ** snowballQuality
#     if snowballValue > m_value:
#         result = f'{snowballSnow} : {snowballTime} = {snowballValue} ({snowballQuality})'
#         m_value = snowballValue
#
# print(result)

# 10. Gladiator Expenses
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helm_broken = 0
sword_broken = 0
sheild_broken = 0
armor_broken = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        helm_broken += 1
    if i % 3 == 0:
        sword_broken += 1
    if i % 6 == 0:
        sheild_broken += 1
    if i % 12 == 0:
        armor_broken += 1

expenses = helm_broken * helmet_price + sword_broken * sword_price + \
           sheild_broken * shield_price + armor_broken * armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')

































































