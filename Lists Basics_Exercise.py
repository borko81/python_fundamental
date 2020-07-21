# 01. Invert Values
# numbers = input().split(' ')
# print([int(i) * -1 for i in numbers])

# 02. Multiples List
# factor = int(input())
# count = int(input())
# print([i * factor for i in range(1, count + 1)])

# 03. Football Cards
# A = [i for i in range(1, 12)]
# B = [i for i in range(1, 12)]
#
# card = input().split(' ')
#
# for i in card:
#     team, player = i.split('-')
#     if team == 'A':
#         try:
#             A.remove(int(player))
#         except:
#             pass
#     else:
#         try:
#             B.remove(int(player))
#         except:
#             pass
#
# print(f'Team A - {len(A)}; Team B - {len(B)}')
# if len(A) < 7 or  len(B) < 7:
#     print('Game was terminated')

# 04. Number Beggers
# l = [int(i) for i in input().split(', ')]
# num = int(input())
#
# result = [[0] for _ in range(num)]
# count = 0
#
# for i in range(len(l)):
#     result[i].extend(l[i::num])
#     count += 1
#     if count == num:
#         break
#
# print([sum(i) for i in result])

# 05. Faro Shuffle
# l = input().split(' ')
# n = int(input())
#
# chunk = len(l) // 2
#
# for _ in range(n):
#     res = []
#     for i in range(chunk):
#         res.append(l[i])
#         res.append(l[i+chunk])
#     l = res
#
# print(l)

# 06. Survival of the Biggest
# numbers = [int(i) for i in input().split(' ')]
# n = int(input())
# def main():
#     m = numbers[0]
#     for _ in numbers:
#         if _ < m:
#             m = _
#     numbers.remove(m)
#
# for _ in range(n):
#     main()
#
# print(numbers)

# 07. Easter Gifts
# names = input().split(' ')
# result = []
#
# while True:
#     line = input()
#     if line == 'No Money':
#         break
#
#     if line.startswith('OutOfStock'):
#         search = line.split(' ')[1]
#         for _, n in enumerate(names):
#             if n == search:
#                 names[_] = 'None'
#
#     if line.startswith('Required'):
#         _, gift, ind = line.split(' ')
#         ind = int(ind)
#         if 0 < ind < len(names):
#             names[ind] = gift
#
#     if line.startswith('JustInCase'):
#         _, val = line.split(' ')
#         names[-1] = val
#
#
# while 'None' in names:
#     names.remove('None')
#
# print(" ".join(names))


# 08. Seize the Fire
# fires = input().split('#')
# water = int(input())
# """
# Type of Fire Range
# High
#             81 - 125
# Medium
#             51 - 80
# Low
#             1 - 50
# """
#
# result = []
# effort = 0
# total_fire = 0
#
# for _ in fires:
#     f, w = _.split(' = ')
#     w = int(w)
#     if water < w:
#         continue
#
#     if f == 'High' and 81 <= w <= 125:
#         result.append(w)
#         water -= w
#         effort += w * 0.25
#         total_fire += w
#     if f == 'Medium' and 51 <= w <= 80:
#         result.append(w)
#         water -= w
#         effort += w * 0.25
#         total_fire += w
#     if f == 'Low' and 1 <= w <= 50:
#         result.append(w)
#         water -= w
#         effort += w * 0.25
#         total_fire += w
#
# print("Cells:")
#
# for cell in result:
#     print(f' - {cell}')
#
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {total_fire}')

# 09. Hello, France
# clotes = input().split('|')
# budjet = float(input())
#
# result = []
#
# for _ in clotes:
#     name,price = _.split('->')
#     price = float(price)
#     if name == 'Clothes' and price > 50:
#         continue
#     if name == 'Shoes' and price > 35:
#         continue
#     if name == 'Accessories' and price > 20.5:
#         continue
#
#     if price <= budjet:
#         budjet -= price
#         result.append(price)
#
# result_with_40_percent = [float(f'{(i + i * 0.40):.2f}') for i in result]
# new_budjet = budjet + sum(result_with_40_percent)
#
# for _ in result_with_40_percent:
#     print(f'{_:.2f}', end=' ')
# print()
#
# profit = sum(result_with_40_percent) - sum(result)
# print(f'Profit: {profit:.2f}')
#
# if new_budjet >= 150:
#     print(f'Hello, France!')
# else:
#     print(f'Time to go.')

# 10. Bread Factory
# energy = 100
# coins = 100
# bankrut = False
#
# line = input().split('|')
#
# for _ in line:
#     if bankrut == True:
#         continue
#     order, score = _.split('-')
#     score = int(score)
#     if order == 'rest':
#         current_energy = 0
#         if energy + score < 100:
#             current_energy = score
#             energy += score
#         else:
#             current_energy = 100 - energy
#             energy = 100
#         print(f'You gained {current_energy} energy.')
#         print(f'Current energy: {energy}.')
#
#     elif order == 'order':
#         if energy >= 30:
#             coins += score
#             energy -= 30
#             print(f'You earned {score} coins.')
#         else:
#             energy += 50
#             print(f'You had to rest!')
#             continue
#
#     else:
#         if coins <= score:
#             print(f'Closed! Cannot afford {order}.')
#             bankrut = True
#             break
#         coins -= score
#         print(f'You bought {order}.')
#
#
# if bankrut == False:
#     print(f'Day completed!')
#     print(f'Coins: {coins}')
#     print(f'Energy: {energy}')














































