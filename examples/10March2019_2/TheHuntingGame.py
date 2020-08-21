'''
First you will receive the days of the adventure, the count of the players and the group’s energy. Afterwards, you will
 receive the following provisions per day for one person:
    • Water
    • Food
The group calculates how many supplies they’d need for the adventure and take that much water and food.
Every day they chop wood and lose a certain amount of energy. For each of the days, you are going to receive the energy
loss from chopping wood. The program should end If the energy reaches 0 or less.
Every second day they drink water, which boosts their energy with 5% of their current energy and at the same time drops
their water supplies by 30% of their current water.
Every third day they eat, which reduces their food supplies by the following amount:
{currentFood} / {countOfPeople} and at the same time raises their group’s energy by 10%.
The chopping of wood, the drinking of water, and the eating happen in the order above.
If they have enough energy to finish the quest, print the following message:
"You are ready for the quest. You will be left with - {energyLevel} energy!"
If they run out of energy print the following message and the food and water they were left with before they ran out of
energy:
"You will run out of energy. You will be left with {food} food and {water} water."
'''

day_of_campain = int(input())
players = int(input())
group_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

total_woter = day_of_campain * players * water_per_day_for_one_person
total_food = day_of_campain * players * food_per_day_for_one_person

for day in range(1, day_of_campain + 1):

    group_energy -= float(input())

    if group_energy <= 0 :
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_woter:.2f} water.')
        break

    if day % 2 == 0:
        group_energy *= 1.05
        total_woter -= total_woter * 0.3

    if day % 3 == 0:
        group_energy *= 1.1
        total_food -= total_food / players


if group_energy > 0:
    print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')