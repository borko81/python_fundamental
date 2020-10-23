budget = float(input())
price_flour = float(input())

info = {
    'Eggs': 1,
    'Floor': 1,
    'Milk': 0.250
}

make = 0
colored_eggs = 0

price_eggs = price_flour * 0.75
price_milk = (price_flour + price_flour * 0.25) / 4

total_amount = price_milk + price_eggs + price_flour


while budget > total_amount:
    budget -= total_amount
    make += 1
    colored_eggs += 3
    if make % 3 == 0:
        colored_eggs -= make - 2



print(f'You made {make} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')


'''
Create a program that calculates how much cozonacs you can make with the budget you have. First, you will receive your
budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one cozonac:
Eggs
1 pack
Flour
1 kg
Milk
0.250 l
The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than price for 1 kg
flour. Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
    • For every cozonac that you make, you will receive 3 colored eggs. 
    • For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the usual
      3 colored eggs for your cozonac. The count of eggs you will lose is calculated when you subtract 2 from your
      current count of cozonacs – ({currentCozonacsCount} – 2)
In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, formatted to the 2nd 
decimal place, in the following format:
"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."'''