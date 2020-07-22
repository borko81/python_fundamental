# 01. Zeros to Back
# s = [int(i) for i in input().split(', ')]
#
# for i in s:
#     if i == 0:
#         s.remove(i)
#         s.append(i)
#
# print(s)

# 02. Tic-Tac-Toe
# line_one = [int(i) for i in input().split()]
# line_two = [int(i) for i in input().split()]
# line_three = [int(i) for i in input().split()]
#
#
# if line_one[0] == line_one[1] == line_one[2] == 1:
#     print('First player won')
# elif line_one[0] == line_one[1] == line_one[2] == 2:
#     print('Second player won')
#
# elif line_two[0] == line_two[1] == line_two[2] == 1:
#     print('First player won')
# elif line_two[0] == line_two[1] == line_two[2] == 2:
#     print('Second player won')
#
# elif line_one[0] == line_three[1] == line_three[2] == 2:
#     print('Second player won')
# elif line_one[0] == line_three[1] == line_three[2] == 1:
#     print('First player won')
#
# elif line_one[0] == line_two[0] == line_three[0] == 2:
#     print('Second player won')
# elif line_one[0] == line_two[0] == line_three[0] == 1:
#     print('First player won')
#
# elif line_one[1] == line_two[1] == line_three[1] == 2:
#     print('Second player won')
# elif line_one[1] == line_two[1] == line_three[1] == 1:
#     print('First player won')
#
# elif line_one[2] == line_two[2] == line_three[2] == 2:
#     print('Second player won')
# elif line_one[2] == line_two[2] == line_three[2] == 1:
#     print('First player won')
#
# elif line_one[0] == line_two[1] == line_three[2] == 2:
#     print('Second player won')
# elif line_one[0] == line_two[1] == line_three[2] == 1:
#     print('First player won')
#
# elif line_one[2] == line_two[1] == line_three[0] == 2:
#     print('Second player won')
# elif line_one[2] == line_two[1] == line_three[0] == 1:
#     print('First player won')
#
# else:
#     print('Draw!')

# 03. Josephus Permutation
# s = [int(i) for i in input().split(' ')]
# k = int(input())
#
# result = []
# index = 0
# counter = 0
#
# while len(s) > 0:
#     counter += 1
#     if counter % k == 0:
#         result.append(s.pop(index))
#     else:
#         index += 1
#
#     if index >= len(s):
#         index = 0
#
# print(str(result).replace(' ', ''))

# 04. Battle Ships
# n = int(input())
# deck = [[] for _ in range(n)]
#
# for x in range(0, n):
#     deck[x].extend([int(i) for i in input().split(' ')])
#
# ship_destroy = 0
# target = input().split(' ')
#
# for _ in target:
#     ship = 0
#     result = _.split('-')
#     row = int(result[0])
#     col = int(result[1])
#     ship = deck[row][col]
#     ship -= 1
#     deck[row][col] = ship
#     if ship == 0:
#         ship_destroy += 1
#
# print(ship_destroy)

# 05. Hungry Hippos
deck = [
    [1, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0]
]

result = 0

for r in range(len(deck)):
    for c in range(len(deck[r])):
        print(deck[r][c], end='')
    print()

























