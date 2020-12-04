target_towns = {}

while True:
    command = input()
    if command == 'Sail':
        break

    cities, population, gold, *arg = command.split('||')
    population = int(population)
    gold = int(gold)

    if cities not in target_towns:
        target_towns[cities] = {'population': population, 'gold': gold}
    else:
        target_towns[cities]['population'] += population
        target_towns[cities]['gold'] += gold

while True:
    command = input()
    if command == 'End':
        break

    command = command.split('=>')

    if command[0] == 'Plunder':
        _, town, people, gold, *args = command
        people = int(people)
        gold = int(gold)

        target_towns[town]['population'] -= people
        target_towns[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if target_towns[town]['population'] <= 0 or target_towns[town]['gold'] <= 0:
            del target_towns[town]
            print(f"{town} has been wiped off the map!")

    elif command[0] == 'Prosper':
        _, town, gold, *args = command
        gold = int(gold)

        if gold <= 0:
            print("Gold added cannot be a negative number!")
        else:
            target_towns[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {target_towns[town]['gold']} gold.")

print(f"Ahoy, Captain! There are {len(target_towns)} wealthy settlements to go to:")

for town, value in sorted(target_towns.items(), key=lambda x: (-x[1]['gold'], x[0])):
    print(f"{town} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")

'''
Description
Until the "Sail" command is given you will be receiving:
    • Cities that you and your crew have targeted, with their population and gold, separated by "||".
    • If you receive a city which has been already received, you have to increase the population and gold with the given values.
After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given. 
Events will be in the following format:
    • "Plunder=>{town}=>{people}=>{gold}"
        ◦ You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold. 
        ◦ For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
        ◦ If any of those two values (population or gold) reaches zero, the town is disbanded.
            ▪ You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
        ◦ There will be no case of receiving more people or gold than there is in the city.
    • "Prosper=>{town}=>{gold}"
        ◦ There has been a dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
        ◦ The gold amount can be a negative number, so be careful. If a negative amount of gold is given print: "Gold added cannot be a negative number!" and ignore the command.
        ◦ If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message: "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
Input
    • On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and population, separated by "||"
    • On the next lines, until the "End" command, you will be receiving strings representing the actions described above, separated by "=>"
Output
    • After receiving the "End" command if there are any existing settlements on your list of targets, you need to print all of them, sorted by their gold in descending order, then by their name in ascending order, in the following format:
Ahoy, Captain! There are {count} wealthy settlements to go to:
{town1} -> Population: {people} citizens, Gold: {gold} kg
   …
{town…n} -> Population: {people} citizens, Gold: {gold} kg
    • If there are no settlements left to plunder, print:
"Ahoy, Captain! All targets have been plundered and destroyed!"
'''
