'''
Create a program that calculates the profit after buying some items and selling them on a higher price.
In order to fulfil that, you are going to need certain data - you will receive a collection of items and
  budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a certain price, which is given bellow:
Type
Maximum Price
Clothes
50.00
Shoes
35.00
Accessories
20.50
If a price for a certain item is higher than the maximum price, don’t buy it.
Every time you buy an item, you have to reduce the budget with the value of its price.
If you don’t have enough money for it, you can’t buy it. Buy as much items as you can.
You have to increase the price of each of the items you have successfully bought with 40%.
Print the list with the new prices and the profit you will gain from selling the items.
They need exactly 150$ for tickets for the train, so if their budget after selling the products
is enough – print – "Hello, France!" and if not – "Time to go."
'''

list_item = input().split('|')
budjet = float(input())


prices_items = {'Clothes': 50, 'Shoes': 35, 'Accessories': 20.5}
buy_items = []
cost_item = []

for l in list_item:
    name, price = l.split('->')
    price = float(price)

    if price <= float(prices_items[name]) and price <= budjet and name in prices_items:
        cost_item.append(price)
        buy_items.append(price * 1.4)
        budjet -= price

for item in buy_items:
    print('%.2f' % item, end=' ')

print('')
print(f'Profit: {(sum(buy_items) - sum(cost_item)):.2f}')

if (sum(buy_items) + budjet) >= 150:
    print(f'Hello, France!')
else:
    print(f'Time to go.')