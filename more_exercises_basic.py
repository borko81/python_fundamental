# 01. Find The Largest

# number = input()

# number_to_list = list(number)

# max_num = list(reversed(sorted(number_to_list)))

# print(int("".join(max_num)))

# 02. Find The Capitals

# word = input()
# result = []
# for pos, _ in enumerate(word):
#     if _.isupper():
#         result.append(pos)

# print(result)

# 03. Wolf In Sheep's Clothing

# s = input().split(', ')
# sheep_count = 0

# for pos, animal in enumerate(list(reversed(s))):
#     if animal == 'sheep':
#         sheep_count += 1
#     elif animal == 'wolf':
#         if pos == 0:
#             print('Please go away and stop eating my sheep')
#         else:
#             print(f'Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!')

# 04. Sum Of A Beach

# word = input()
# search_word = ['Sand', 'Water', 'Fish', 'Sun']
# count = 0

# word_to_lower = word.lower()
# search_word_to_lower = [i.lower() for i in search_word]

# for _ in search_word_to_lower:
#     if _ in word_to_lower:
#         count += word_to_lower.count(_)

# print(count)

# 05. How Much Coffee Do You Need?

# search = ['coding', 'dog', 'cat', 'movie']
# count = 0

# while True:
#     line = input()
#     if line == 'END':
#         break
#     if line.lower() in search:
#         if line.isupper():
#             count += 2
#         else:
#             count += 1

# if count > 5:
#     print('You need extra sleep')
# else:
#     print(f'{count}')
