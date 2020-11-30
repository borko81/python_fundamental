from collections import defaultdict

n = int(input())

plantes = {}
planet_with_rating = defaultdict(list)

for _ in range(n):
    line = input()
    planet, rariti = line.split('<->')
    rariti = int(rariti)
    plantes[planet] = rariti
    planet_with_rating[planet] = []

while True:
    command = input()
    if command == 'Exhibition':
        break

    command = command.split(':')

    if command[0] == 'Rate':
        plant, rating = command[1].strip().split(' - ')
        rating = int(rating)
        if plant not in plantes:
            print("error")
        else:
            planet_with_rating[plant].append(rating)

    elif command[0] == 'Update':
        plant, new_rating = command[1].strip().split(' - ')
        new_rating = int(new_rating)

        if plant not in plantes:
            print("error")
        else:
            plantes[plant] = new_rating

    elif command[0] == 'Reset':
        plant = command[1].strip()

        if plant not in planet_with_rating:
            print("error")
        else:
            planet_with_rating[plant] = []

for key, value in planet_with_rating.items():
    if sum(value) > 0 and len(value) > 0:
        planet_with_rating[key] = sum(value) / len(value)
    else:
        planet_with_rating[key] = 0

print("Plants for the exhibition:")

for key, value in sorted(plantes.items(), key=lambda x: (x[1], planet_with_rating[x[0]]), reverse=True):
    print(f"- {key}; Rarity: {value}; Rating: {planet_with_rating[key]:.2f}")

"""On the first line you will receive a number n. On the next n lines, you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information, because you will need it later. If you receive a plant more than once, update its rarity.
After that until you receive the command "Exhibition" you will be given some of these commands:
    • Rate: {plant} - {rating} – add the given rating to the plant (store all ratings)
    • Update: {plant} - {new_rarity} – update the rarity of the plant with the new one
    • Reset: {plant} – remove all the ratings of the given plant
Note: If any of the command is invalid, print "error"
After the command "Exhibition" print the information that you have about the plants in the following format:
Plants for the exhibition:
- {plant_name}; Rarity: {rarity}; Rating: {average_rating formatted to the 2nd digit}
…
The plants should be sorted by rarity descending, then by average rating descending"""

# INPUT
"""
3
Arnoldii<->4
Woodii<->7
Welwitschia<->2
Rate: Woodii - 10
Rate: Welwitschia - 7
Rate: Arnoldii - 3
Rate: Woodii - 5
Update: Woodii - 5
Reset: Arnoldii
Exhibition
"""
