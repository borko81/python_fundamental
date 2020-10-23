shops = input().split()
line_num = int(input())

for _ in range(line_num):
    command = input()
    if command.startswith('Include'):
        c, shop = command.split()
        shops.append(shop)

    elif command.startswith('Visit'):
        c, f_or_l, numbers = command.split()
        numbers = int(numbers)
        if f_or_l == 'first':
            if 0 <= numbers <= len(shops):
                shops = shops[numbers:]


        elif f_or_l == 'last':
            if 0 <= numbers <= len(shops):
                shops = shops[:len(shops) - numbers]


    elif command.startswith('Prefer'):
        c, index_one, index_two = command.split()
        index_one = int(index_one)
        index_two = int(index_two)
        if index_one in range(len(shops)) and index_two in range(len(shops)):
            shops[index_one], shops[index_two] = shops[index_two], shops[index_one]


    elif command.startswith('Place'):
        c, shop, indexs = command.split()
        indexs = int(indexs)
        if indexs + 1 in range(len(shops)):
            shops.insert(indexs + 1, shop)



print('Shops left:')
print(" ".join([i for i in shops]))


'''
Create a program that helps you keep track of the shops that you want to visit. You will receive the list of shops you have planned on checking out on a single line, separated by a single space in the following format:
"{shop1} {shop2} {shop3}… {shopn}"
Then you will receive a number – n - a count of commands you need to execute over your list. There are four possible commands:
    • "Include {shop}":
        ◦ Add the shop at the end of your list.
    • "Visit {first/last} {numberOfShops}"
        ◦ Remove either the "first" or the "last" number of shops from your list, depending on the input. If you have less shops on your list than the given number, skip this command.
    • "Prefer {shopIndex1} {shopIndex2}":
        ◦ If both of the shop indexes exist in your list, take the shops that are on them and change their places. 
    • "Place {shop} {shopIndex}"
        ◦ Insert the shop after the given index, only if the resulted index exists.
In the end print the manipulated list in the following format:
"Shops left:
{shop1} {shop2}… {shopn}"
'''