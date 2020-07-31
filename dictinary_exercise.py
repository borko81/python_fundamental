# 01. Count Chars in a String
# line = input()
# result = {i:line.count(i) for i in line if i != ' '}
# for char, occurrences in result.items():
#     print(f'{char} -> {occurrences}')

# 02. A Miner Task
# count = 1
# result = {}
# while True:
#     line = input()
#     if line == 'stop':
#         break
#     if line not in result:
#         q = int(input())
#         result[line] = q
#     else:
#         q = int(input())
#         result[line] += q
#     count += 1
#
#
# for resource, quantity in result.items():
#     print(f'{resource} -> {quantity}')

# 03. Legendary Farming

# data_fragment = {'Shards': 0, 'Fragments': 0, 'Motes': 0}
# junk = {}
# winner = None
#
# while winner is None:
#     line = input()
#     result = []
#     result.extend(line.split(' '))
#
#     for i in range(0, len(result)-1, 2):
#         item = result[i + 1].lower()
#         if item.capitalize() in data_fragment and winner is None:
#             data_fragment[item.capitalize()] += int(result[i])
#             if data_fragment[item.capitalize()] >= 250:
#                 if item.capitalize() == 'Shards':
#                     winner = 'Shadowmourne'
#                 elif item.capitalize() == 'Fragments':
#                     winner = 'Valanyr'
#                 else:
#                     winner = 'Dragonwrath'
#                 data_fragment[item.capitalize()] -= 250
#                 break
#
#         elif item.capitalize() in data_fragment:
#             data_fragment[item.capitalize()] += int(result[i])
#
#         elif item not in junk and item not in data_fragment and winner is None:
#             junk[item] = int(result[i])
#         elif item in junk and item not in data_fragment and winner is None:
#             junk[item] += int(result[i])
#
#
#
# print(f'{winner} obtained!')
# for material, quantity in sorted(data_fragment.items(), key=lambda x: (-x[1], x[0])):
#     print(f'{material.lower()}: {quantity}')
#
# for material, quantity in sorted(junk.items(), key=lambda x: x[0]):
#     print(f'{material.lower()}: {quantity}')

# 04. Orders
# result = {}
#
# while True:
#     line = input()
#     if line == 'buy':
#         break
#     name, price, quantity = line.split(' ')
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in result:
#         result[name] = [price, quantity]
#     else:
#         if result[name][0] == price:
#             result[name][1] += quantity
#         else:
#             result[name][1] += quantity
#             result[name][0] = price
#
#
# for productName, totalPrice in result.items():
#     print(f'{productName} -> {(totalPrice[0] * totalPrice[1]):.2f}')

# 05. SoftUni Parking
# n = int(input())
# data = {}
#
# for _ in range(n):
#     line = input()
#     if line.startswith('register'):
#         comamnd, name, nomer = line.split(' ')
#         if name not in data:
#             data[name] = nomer
#             print(f'{name} registered {nomer} successfully')
#         else:
#             print(f'ERROR: already registered with plate number {nomer}')
#
#     elif line.startswith('unregister'):
#         command, name = line.split(' ')
#         if name not in data:
#             print(f'ERROR: user {name} not found')
#         else:
#             del data[name]
#             print(f'{name} unregistered successfully')
#
#
# for key, val in data.items():
#     print(f'{key} => {val}')

# 06. Courses
# course = {}
#
# while True:
#     line = input()
#     if line == 'end':
#         break
#     course_name, student_name = line.split(' : ')
#     if course_name not in course:
#         course[course_name] = [student_name]
#     else:
#         course[course_name].append(student_name)
#
#
# for key, val in sorted(course.items(), key=lambda x: len(x[1]), reverse=True):
#     print(f'{key}: {len(val)}')
#     for v in sorted(val):
#         print(f'-- {v}')

# 07. Student Academy
# row = int(input())
# data = {}
#
# for _ in range(row):
#     name = input()
#     grade = float(input())
#     if name not in data:
#         data[name] = [grade]
#     else:
#         data[name].append(grade)
#
# for name, av_grade in sorted(data.items(), key=lambda x: (sum(x[1]) / len(x[1])), reverse=True):
#     av_grade = (sum(av_grade) / len(av_grade))
#     if av_grade >= 4.50:
#         print(f'{name} -> {av_grade:.2f}')

# 08. Company Users
# company = {}
#
# while True:
#     line = input()
#     if line == 'End':
#         break
#     com, id = line.split(' -> ')
#     if com not in company:
#         company[com] = [id]
#     else:
#         if com in company and id not in company[com]:
#             company[com].append(id)
#
# for key, val in sorted(company.items()):
#     print(f'{key}')
#     for v in val:
#         print(f'-- {v}')

# 09. ForceBook
# data = {}
#
# while True:
#     line = input()
#     if line == 'Lumpawaroo':
#         break
#
#     if '|' in line:
#         side, member = line.split(' | ')
#         if side not in data and member not in [i for v in data.keys() for i in data[v]]:
#             data[side] = [member]
#         elif side in data and member not in [i for v in data.keys() for i in data[v]]:
#             data[side].append(member)
#
#     if '->' in line:
#         found = False
#         member, side = line.split(' -> ')
#         if side not in data:
#             data[side] = []
#         for k, v in data.items():
#             for u in v:
#                 if u == member:
#                     v.pop(v.index(u))
#                     data[side].append(member)
#                     found = True
#
#         if found is False:
#             data[side].append(member)
#         print(f'{member} joins the {side} side!')
#
#
# for key, value in sorted(data.items(), key=lambda x: (-len(x[1]),x[0])):
#     if len(value) > 0:
#         print(f'Side: {key}, Members: {len(value)}')
#         for name_user in sorted(value):
#             print(f'! {name_user}')

# 10. SoftUni Exam Results
# data = {}
# users = {}
#
# while True:
#     line = input()
#     if line == 'exam finished':
#         break
#
#     if len(line.split('-')) == 3:
#         username, language, points = line.split('-')
#         points = int(points)
#
#         if language not in data:
#             data[language] = 1
#         else:
#             data[language] += 1
#
#         if username not in users:
#             users[username] = [points]
#         else:
#             users[username].append(points)
#
#     else:
#         username = line.split('-')[0]
#         del users[username]
#
#
# print('Results:')
# for username, points in sorted(users.items(), key=lambda x: (-max(x[1]), x[0])):
#     print(f'{username} | {max(points)}')
#
# print('Submissions:')
# for language, submissionsCount in sorted(data.items(), key=lambda x: (-x[1], x[0])):
#    print(f'{language} - {submissionsCount}')
















































