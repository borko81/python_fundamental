'''
Create a program that calculates travelling expenses by entering the following information:
    • Days of the vacation
    • Budget - its for the whole group
    • The count of people
    • Fuel per kilometer – the price for fuel that their car consumes per kilometer
    • Food expenses per person
    • Hotel room price for one night – again, for one person
If the group is bigger than 10, they receive a 25% discount from the total hotel expenses.
Every day, they travel some distance and you have to calculate the expenses for the travelled kilometers.
Every third and fifth day, they have some additional expenses, which are 40% of the current value of the expenses.
Every seventh day, their expenses are reduced, because they withdraw (receive) a small amount of money – you can calculate it by dividing the amount of the current expenses by the group of people.
If the expenses exceed the budget at some point, stop calculating and print the following message:
"Not enough money to continue the trip"
If the budget is enough:
"You have reached the destination. You have {money}$ budget left."
Print the result formatted 2 digits after the decimal separator.
'''

day_of_trip = int(input())
budjet = float(input())
people = int(input())
price_kilometer = float(input())
food = float(input())
room_price = float(input())

if people > 10:
    room_price *= 0.75


trip_money = people * day_of_trip * (room_price + food)

for day in range(1, day_of_trip + 1):
    day_expense = 0
    km = float(input()) * price_kilometer
    trip_money += km

    if day % 3 == 0 or day % 5 == 0:
        trip_money += trip_money * 0.4

    if day % 7 == 0:
        trip_money -= trip_money / people

    if trip_money > budjet:
        print(f'Not enough money to continue the trip. You need {(trip_money - budjet):.2f}$ more.')
        break


if trip_money <= budjet:
    print(f'You have reached the destination. You have {(budjet - trip_money):.2f}$ budget left.')
