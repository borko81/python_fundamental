# 01. Bakery
# data = input().split(' ')
# k = data[0:len(data):2]
# v = [int(i) for i in data[1:len(data):2]]
# print(dict(zip(k, v)))

# 02. Stock
# product = input().split(' ')
# search_item = [i for i in input().split(' ')]
# k = product[0:len(product):2]
# v = [int(i) for i in product[1:len(product):2]]
# data = dict(zip(k, v))
#
#
# def check_product(product):
#     if product in data:
#         print(f'We have {data[product]} of {product} left')
#     else:
#         print(f'Sorry, we don\'t have {product}')
#
#
# for item in search_item:
#     check_product(item)

# 03 Statistics
# data = {}
#
# while True:
#     line = input()
#     if line == 'statistics':
#         print('Products in stock:')
#         for k, v in data.items():
#             print(f'- {k}: {v}')
#         print(f'Total Products: {len(data.keys())}')
#         print(f'Total Quantity: {sum(data.values())}')
#         break
#     else:
#         key, val = line.split(': ')
#         val = int(val)
#         if key in data.keys():
#             data[key] += val
#         else:
#             data[key] = val

# 04. Odd Occurrences
# sentence = input().split()
# data = {}
#
# for key in sentence:
#     key = key.lower()
#     if key not in data:
#         data[key] = 1
#     else:
#         data[key] += 1
#
# print(" ".join([i for i, k in data.items() if k & 1]))

# 05. Word Synonyms
n = int(input())
data = dict()

for i in range(n):
    key = input()
    val = input()
    if key in data:
        data[key].append(val)
    else:
        data[key] = [val]

for k, v in data.items():
    print(f'{k} - {", ".join(v)}')

























