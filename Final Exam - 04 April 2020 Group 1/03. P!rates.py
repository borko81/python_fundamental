targets = dict()

while True:
    line = input()
    if line == 'Sail':
        break

    target, population, gold = line.split('||')
    population = int(population)
    gold = int(gold)

    if target not in targets:
        targets[target] = [population, gold]
    else:
        targets[target][0] += population
        targets[target][1] += gold


while True:
    events = input()
    if events == 'End':
        break

    events = events.split('=>')

    if events[0] == 'Plunder':
        target, town, people, gold = events
        people = int(people)
        gold = int(gold)

        if town in targets:
            print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
            targets[town][0] -= people
            targets[town][1] -= gold

            if targets[town][0] <= 0 or targets[town][1] <= 0:
                print(f'{town} has been wiped off the map!')
                del targets[town]

    elif events[0] == 'Prosper':
        town, gold = events[1:]
        gold = int(gold)
        if town in targets and gold >= 0:
            targets[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold.')
        elif town in targets and gold < 0:
            print('Gold added cannot be a negative number!')


print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')

for town, values in sorted(targets.items(), key=lambda x: (-x[1][1], x) ):
    people = values[0]
    gold = values[1]
    print(f'{town} -> Population: {people} citizens, Gold: {gold} kg')