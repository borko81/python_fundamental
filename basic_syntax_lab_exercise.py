#Big number
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > b > c:
#     print(a)
# elif b > a > c:
#     print(b)
# else:
#     print(c)

#02. Number Definer
# number = float(input())
# if number == 0:
#     print("zero")
# elif number > 0:
#     if abs(number) < 1:
#         print(f'small positive')
#     elif abs(number) > 1000000:
#         print(f'large positive')
#     else:
#         print('positive')
# elif number < 0:
#     if abs(number) < 1:
#         print(f'small negative')
#     elif abs(number) > 1000000:
#         print(f'large negative')
#     else:
#         print('negative')

#03. Word Reverse
# word = input()
# print("".join(reversed(word)))

#Number Between 1 and 100
# while True:
#     n = float(input())
#     if 1 <= n <= 100:
#         print(f'The number {n} is between 1 and 100')
#         break

#05. Patterns
# n = int(input())
#
# for r in range(1, n + 1):
#     print('*' * r)
# for r in range(n - 1, 0, -1):
#     print('*' * r)

#01 Jenny's Secret Message
# name = input()
# if name == 'Johnny':
#     print('Hello, my love!')
# else:
#     print(f'Hello, {name}!')

#02. Drink Something
# n = int(input())
#
# if 1 < n <= 14:
#     print('drink toddy')
# elif 14 < n <= 18:
#     print('drink coke')
# elif 18 < n <= 21:
#     print('drink beer')
# elif n > 21:
#     print('drink whisky')

#03. Leonardo DiCaprio Oscars
# n = int(input())
# if n == 88:
#     print(f'Leo finally won the Oscar! Leo is happy')
# elif n == 86:
#     print('Not even for Wolf of Wall Street?!')
# elif n > 88:
#     print('Leo got one already!')
# else:
#     print('When will you give Leo an Oscar?')

#04. Double Char
# word = input()
# new_word = ''
#
# for _ in word:
#     new_word += f'{_}{_}'
#
# print(new_word)

#05. Can't Sleep? Count Sheep
# n = int(input())
# for i in range(1, n + 1):
#     print(f'{i} sheep...', end='')

#06. Next Happy Year
# n = int(input())
# while True:
#     n += 1
#     n_s = str(n)
#     if len(set(n_s)) == len(n_s):
#         print(int(n_s))
#         break

#07. Maximum Multiple
# n = int(input())
# b = int(input())
# result = []
#
# for _ in range(n, b + 1):
#     if _ / n == _ // n:
#         result.append(_)
#
# print(result[-1])

#08. Mutate Strings
# f = list(input())
# s = list(input())
#
# for i in range(len(f)):
#     if f[i] != s[i]:
#         f[i], s[i] = s[i], f[i]
#         print("".join(f))


#09. Easter Cozonacs
# budjet = float(input())
# floor_price = float(input())
#
# eggs_price = floor_price * 0.75
# milk_price = ((floor_price + floor_price * 0.25) / 1000) * 250
# total_price = floor_price + eggs_price + milk_price
#
# total_cozunak = 0
# collored_eggs = 0
#
# while True:
#     if total_price < budjet:
#         budjet -= total_price
#         total_cozunak += 1
#         if total_cozunak % 3 == 0:
#             collored_eggs += 3
#             collored_eggs -= (total_cozunak - 2)
#         else:
#             collored_eggs += 3
#     else:
#         print(f'You made {total_cozunak} cozonacs! Now you have {collored_eggs} eggs and {budjet:.2f}BGN left.')
#         break

#10. Christmas Spirit
# quntity = int(input())
# days = int(input())
#
# budjet = 0
# spirit = 0
# d = 0
#
# for _ in range(1, days + 1):
#     d += 1
#     if _ % 11 == 0:
#         quntity += 2
#
#     if _ % 2 == 0:
#         budjet += (2 * quntity)
#         spirit += 5
#
#     if _ % 3 == 0:
#         budjet += ((5 * quntity) + (3 * quntity))
#         spirit += 13
#
#     if  _ % 5 == 0:
#         budjet += 15 * quntity
#         spirit += 17
#         if _ % 3 == 0:
#             spirit += 30
#
#     if  _ % 10 == 0:
#         budjet += (5 + 3 + 15)
#         spirit -= 20
#
#
# if d % 10 == 0:
#     spirit -= 30
#
# print(f'Total cost: {budjet}')
# print(f'Total spirit: {spirit}')













































































