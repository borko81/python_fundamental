'''
"Enroll {HeroName}":
    • Adds the hero to your collection of heroes.
    • If the hero is already present in your collection, print: "{HeroName} is already enrolled."
"Learn {HeroName} {SpellName}":
    • Adds the {SpellName} to the {HeroName}'s spellbook.
    • If the {HeroName} doesn’t exist in the collection, print: "{HeroName} doesn't exist."
    • If the hero already has the spell in his spellbook print: "{HeroName} has already learnt {SpellName}."
"Unlearn {HeroName} {SpellName}":
    • Remove the {SpellName} from the {HeroName}'s spellbook.
    • If the {HeroName} doesn’t exist in the collection, print: "{HeroName} doesn't exist."
    • If the {SpellName} doesn't exist in the hero's spellbook, print: "{HeroName} doesn't know {SpellName}."

After you receive the "End" command, print all the heroes sorted by their count of spells in descending and then by the hero name ascending in the format described below:

"Heroes:
== {name1}: {spell1}, {spell2}, {spelln}
== {name2}: {spell1}, {spell2}, {spelln}
...
== {nameN}: {spell1}, {spell2}, {spelln}
'''



heroes = dict()


def enroll(heroes, HeroName):
    if HeroName not in heroes:
        heroes[HeroName] = []
    else:
        print(f'{HeroName} is already enrolled.')
    return heroes


def learn(heroes, HeroName, SpellName):
    if HeroName not in heroes:
        print(f'{HeroName} doesn\'t exist.')
    elif HeroName in heroes and SpellName not in heroes[HeroName]:
        heroes[HeroName].append(SpellName)
    else:
        print(f'{HeroName} has already learnt {SpellName}.')
    return heroes


def unlearn(heroes, HeroName, SpellName):
    if HeroName not in heroes:
        print(f'{HeroName} doesn\'t exist.')
    elif HeroName in heroes and SpellName not in heroes[HeroName]:
        print(f'{HeroName} doesn\'t know {SpellName}.')
    else:
        heroes[HeroName].remove(SpellName)
    return heroes


while True:
    command = input().split()
    if command[0] == 'End':
        break

    if command[0] == 'Enroll':
        _, HeroName = command
        heroes = enroll(heroes, HeroName)

    elif command[0] == 'Learn':
        _, HeroName, SpellName = command
        heroes = learn(heroes, HeroName, SpellName)

    elif command[0] == 'Unlearn':
        _, HeroName, SpellName = command
        heroes = unlearn(heroes, HeroName, SpellName)


print('Heroes:')
for key, value in sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]) ):
    print(f'== {key}: {", ".join(i for i in value)}')