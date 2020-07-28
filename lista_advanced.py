# 01. Trains
# n = int(input())
# l = [0 for _ in range(n)]
#
# while True:
#     line = input()
#     if line == 'End':
#         break
#
#     if line.startswith('add'):
#         people = line.split(' ')[1]
#         l[-1] += int(people)
#
#     if line.startswith('insert'):
#         index = line.split(' ')[1]
#         people = line.split(' ')[2]
#         l[int(index)] += int(people)
#
#     if line.startswith('leave'):
#         index = line.split(' ')[1]
#         people = line.split(' ')[2]
#         l[int(index)] -= int(people)
#
# print(l)

# 02. Todo List
# l = {}
# command = input()
#
# while command != 'End':
#     tokens = command.split('-')
#     l[int(tokens[0])] = tokens[1]
#     command = input()
#
# print([i[1] for i in sorted(l.items())])

# 03. Palindrome Strings
# words = input().split(' ')
# searched = input()
# result = [i for i in words if i == "".join(reversed(i))]
#
# print(result)
# print(f'Found palindrome {words.count(searched)} times')

# 04. Even Numbers
# numbers = [int(i) for i in input().split(', ')]
# print([i for i, n in enumerate(numbers) if n % 2 == 0])

# 05. The Office
# employe = [int(i) for i in input().split(' ')]
# happy = int(input())
#
# employe = [i* happy for i in employe]
# average = sum(employe) // len(employe)
# employes = [i for i in employe if i > average]
# happy_emp = len(employes)
# total_employe = len(employe)
#
# if happy_emp >= total_employe // 2:
#     print(f'Score: {happy_emp}/{total_employe}. Employees are happy!')
# else:
#     print(f'Score: {happy_emp}/{total_employe}. Employees are not happy!')

# 04. Office Chairs
# n = int(input())
#
# chairs = 0
# free_seats = 0
# NOT_ERROR = True
#
# for i in range(1, n + 1):
#     line = input().split(' ')
#     chair = line[0]
#     free = int(line[1])
#     if len(chair) == free:
#         continue
#     elif len(chair) > free:
#         chairs += len(chair) - free
#     elif len(chair) < free:
#         NOT_ERROR = False
#         print(f'{free - len(chair)} more chairs needed in room {i}')
#
# if NOT_ERROR:
#     print(f'Game On, {chairs} free chairs left')

# 05. Electron Distribution
# [2, 8, 18, 32, 50, 72, 98, 128, 162]
# n = int(input())
# result = []
# counter = 1
#
# while n != 0:
#     variant = 2*(counter**2)
#     if variant < n:
#         result.append(variant)
#         n -= variant
#     else:
#         result.append(n)
#         n = 0
#     counter += 1
#
# print(result)

# 06. Group of 10's
# numbers = [int(i) for i in input().split(', ')]
# result = {}
# max = max(numbers)
#
# for i in range(10, max + 10, 10):
#     result[i] = []
#
# for _ in numbers:
#     check = (_ // 10)
#     if check == _ / 10:
#         result[check * 10].append(_)
#     else:
#         result[(check + 1) * 10].append(_)
#
# for k, v in result.items():
#     print(f"Group of {k}'s: {v}")

# 07. Decipher this!
# words = input().split(' ')
#
# result = []
#
# for word in words:
#     w = list(word)
#     d = []
#     for _ in w:
#         if _.isdigit():
#             d.append(_)
#     w = w[len(d):]
#     f_w = chr(int("".join(d)))
#     w[0], w[-1] = w[-1], w[0]
#     w = f_w + "".join(w)
#     result.append(w)
#
# print(" ".join(result))

# 08. Feed the Animals
# line = input()
#
# animals_name = []
# animals_food = []
# animals_area = {}
#
# while line != 'Last Info':
#
#     choice, name, food, area = line.split(":")
#     food = int(food)
#
#     if choice == 'Add':
#         if name in animals_name:
#             index = animals_name.index(name)
#             animals_food[index] += food
#         else:
#             animals_name.append(name)
#             animals_food.append(food)
#             if area not in animals_area:
#                 animals_area[area] = 1
#             else:
#                 animals_area[area] += 1
#
#     if choice == 'Feed':
#         if name in animals_name:
#             index = animals_name.index(name)
#             animals_food[index] -= food
#             if animals_food[index] <= 0:
#                 animals_name.pop(index)
#                 animals_food.pop(index)
#                 animals_area[area] -= 1
#                 if animals_area[area] == 0:
#                     del animals_area[area]
#                 print(f'{name} was successfully fed')
#
#     line = input()
#
#
# z = list(zip(animals_name, animals_food))
# all_zip = sorted(sorted(z, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
# print('Animals:')
# for n in all_zip:
#     print(f"{n[0]} -> {n[1]}g")
#
# print('Areas with hungry animals:')
#
# for i in sorted(animals_area.items(), key=lambda x: -x[1]):
#     print(f'{i[0]} : {i[1]}')

# 09. On the Way to Annapurna
# s = []
# i = []
#
# while True:
#     line = input()
#     if line == 'END':
#         break
#     if line.startswith('Add'):
#         line = line.split('->')
#         comamnd = line[0]
#         store = line[1]
#         item = line[2].split(',')
#         if store not in s:
#             s.append(store)
#             i.append([i for i in item])
#         else:
#             index = s.index(store)
#             i[index].extend([i for i in item])
#     elif line.startswith('Remove'):
#         line = line.split('->')
#         comamnd = line[0]
#         store = line[1]
#         if store in s:
#             index = s.index(store)
#             s.pop(index)
#             i.pop(index)
#
#
# z = sorted(list(zip(s, i)), key=lambda x: (len(x[1]), x[0]), reverse=True)
#
# print('Stores list:')
# for r in z:
#     print(r[0])
#     for _ in r[1]:
#         print(f'<<{_}>>')

# 10. Man O War
# pirate_ship = [int(i) for i in input().split('>')]
# warship = [int(i) for i in input().split('>')]
# health = int(input())
#
# to_repair_soon = health * 0.2
# lost = False
#
# while True:
#     line = input()
#     if line == 'Retire':
#         break
#
#     if line.startswith('Fire'):
#         line = line.split(' ')
#         command = line[0]
#         index = int(line[1])
#         demage = int(line[2])
#         if 0 <= index < len(warship):
#             warship[index] -= demage
#
#             if warship[index] <= 0:
#                 print(f'You won! The enemy ship has sunken.')
#                 lost = True
#                 break
#
#     elif line.startswith('Defend'):
#         line = line.split(' ')
#         command = line[0]
#         start = int(line[1])
#         end = int(line[2])
#         demage = int(line[3])
#         if start >=0 and start < len(pirate_ship) and end >=0 and end < len(pirate_ship):
#             for _ in range(start, end + 1):
#                 pirate_ship[_] -= demage
#                 if pirate_ship[_] <= 0:
#                     print(f'You lost! The pirate ship has sunken.')
#                     lost = True
#                     break
#             if lost:
#                 break
#
#     elif line.startswith('Repair'):
#         line = line.split(' ')
#         command = line[0]
#         index = int(line[1])
#         demage = int(line[2])
#         if 0 <= index < len(pirate_ship):
#             if pirate_ship[index] + demage < health:
#                 pirate_ship[index] += demage
#             else:
#                 pirate_ship[index] = health
#
#     elif line.startswith('Status'):
#         rep = [a for a in pirate_ship if a < to_repair_soon]
#         print(f'{len(rep)} sections need repair.')
#
#
# if lost == False:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(warship)}")

# 01. Messaging
# numbers = input().split(' ')
# text = list(input())
#
# result = []
# word = ''
# for _ in numbers:
#     s = sum(int(i) for i in _)
#     result.append(s)
#
# for _ in result:
#     l = len(text)
#     if _ >= l:
#         a = text.pop(_ - len(text))
#         word += a
#     else:
#         a = text.pop(_)
#         word += a
#
#
# print(word)

# 02. Car Race
# race = [int(i) for i in input().split(' ')]
# finish = len(race) // 2
# f_car = race[0:finish]
# s_car = race[-1:finish:-1]
#
# score_f_car = 0
# score_s_car = 0
#
# for _ in f_car:
#     score_f_car += _
#     if _ == 0:
#         score_f_car *= 0.8
#
#
#
# for _ in s_car:
#     score_s_car += _
#     if _ == 0:
#         score_s_car *= 0.8
#
#
# if score_f_car > score_s_car:
#     print(f"The winner is right with total time: {score_s_car:.1f}")
# else:
#     print(f"The winner is left with total time: {score_f_car:.1f}")

# 03. Take/Skip Rope
# message = list(input())
# digit_list = []
#
# for index, character in enumerate(message):
#     if character.isdigit():
#         digit_list.append(character)
#
# message = [i for i in message if not i.isdigit()]
# take_list = [int(i) for i in digit_list[0:len(message)+1:2]]
# skip_list = [int(i) for i in digit_list[1:len(message)+1:2]]
# word = []
#
# take = 0
# for i in list(zip(take_list, skip_list)):
#     t = i[0] + i[1]
#     word.extend(message[take:take + i[0]])
#     take += t
#
# print("".join(word))

# 04. Social Distribution
# population = [int(i) for i in input().split(', ')]
# wealth = int(input())
# good = True
#
# for i in range(len(population)):
#     if population[i] < wealth:
#         diff = wealth - population[i]
#         m = max(population)
#         if m - diff >= wealth:
#             population[population.index(m)] -= diff
#             population[i] += diff
#         else:
#             good = False
#
# if good:
#     print(population)
# else:
#     print('No equal distribution possible')

# 05. Kate's Way Out





























