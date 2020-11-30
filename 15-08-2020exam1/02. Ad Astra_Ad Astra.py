import re

pattern = re.compile(r'([#|\|])(?P<name>[a-zA-Z\s]+)\1(?P<days>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1')

single_string = input()

# Constraint
names = []
calories = []
days = []
needed_calories = 2000

for s in pattern.finditer(single_string):
    name = s.group('name')
    day = s.group('days')
    calorie = s.group('calories')
    names.append(name)
    calories.append(calorie)
    days.append(day)

cal_for_days = sum([int(i) for i in calories]) // needed_calories

print(f"You have food to last you for: {cal_for_days} days!")
data = list(zip(names, calories, days))

if cal_for_days >= 1:
    for name, d, values in data:
        print(f"Item: {name}, Best before: {values}, Nutrition: {d}")

"""
On the first line of the input you will be given a text string. You must extract the information about the food and calculate the total calories. 
First you must extract the food info. It will always follow the same pattern rules:
    • It will be surrounded by "|" or "#" (only one of the two) in the following pattern: 
#{item name}#{expiration date}#{calories}#   or 
|{item name}|{expiration date}|{calories}|
    • The item name will contain only lowercase and uppercase letters and whitespace
    • The expiration date will always follow the pattern: {day}/{month}/{year}, where the day, month and year will be exactly two digits long
    • The calories will be an integer between 0-10000
Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day."""
