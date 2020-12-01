number_of_heroes = int(input())

heroes = {}
MAX_HP = 100
MAX_MP = 200

for _ in range(number_of_heroes):
    hero, HP, MP = input().split()
    HP = int(HP)
    MP = int(MP)
    if hero not in heroes:
        heroes[hero] = [HP, MP]
    else:
        heroes[hero][0] += HP
        heroes[hero][1] += MP

while True:
    command = input()
    if command == 'End':
        break

    command = command.split(' - ')

    if command[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = command[1:]
        mp_needed = int(mp_needed)

        if hero_name in heroes:
            if heroes[hero_name][1] < mp_needed:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
            else:
                heroes[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1:]
        damage = int(damage)
        if hero_name in heroes:
            temp = heroes[hero_name][0] - damage
            if temp <= 0:
                del heroes[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")
            else:
                heroes[hero_name][0] -= damage
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")

    elif command[0] == 'Recharge':
        hero_name, amount = command[1:]
        amount = int(amount)
        if hero_name in heroes:
            temp = heroes[hero_name][1] + amount
            if temp > MAX_MP:
                amount = MAX_MP - heroes[hero_name][1]
                heroes[hero_name][1] = MAX_MP
            else:
                heroes[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        hero_name, amount = command[1:]
        amount = int(amount)
        if hero_name in heroes:
            temp = heroes[hero_name][0] + amount
            if temp > MAX_HP:
                amount = MAX_HP - heroes[hero_name][0]
                heroes[hero_name][0] = MAX_HP
            else:
                heroes[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")

for key, value in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
