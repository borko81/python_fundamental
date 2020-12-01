number_of_heroes = int(input())

heroes = {}
MAX_HP = 100
MAX_MP = 200

for _ in range(number_of_heroes):
    [hero, HP, MP] = input().split(" ")
    HP = int(HP)
    MP = int(MP)
    heroes[hero] = [HP, MP]

while True:
    command = input()
    if command == 'End':
        break

    command = [i.strip() for i in command.split(" - ")]

    if command[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = command[1:]
        mp_needed = int(mp_needed)

        if mp_needed <= heroes[hero_name][1]:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker, *args = command[1:]
        damage = int(damage)

        temp = heroes[hero_name][0] - damage
        if temp > 0:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == 'Recharge':
        hero_name, amount, *args = command[1:]
        amount = int(amount)

        temp = heroes[hero_name][1] + amount
        if temp >= MAX_MP:
            amount = MAX_MP - heroes[hero_name][1]
            heroes[hero_name][1] = MAX_MP
        else:
            heroes[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        hero_name, amount, *args = command[1:]
        amount = int(amount)

        temp = heroes[hero_name][0] + amount
        if temp >= MAX_HP:
            amount = MAX_HP - heroes[hero_name][0]
            heroes[hero_name][0] = MAX_HP
        else:
            heroes[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")

if heroes:
    for key, value in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
        print(key)
        print(f"  HP: {value[0]}")
        print(f"  MP: {value[1]}")
