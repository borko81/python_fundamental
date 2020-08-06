data = {}

while True:
    line = input()
    if line == 'Once upon a time':
        break

    dwarfName, dwarfHatColor, Physics = line.split(' <:> ')
    dwarfPhysics = int(Physics)

    if dwarfHatColor not in data:
        data[dwarfHatColor] = {dwarfName: dwarfPhysics}

    elif dwarfHatColor in data and dwarfName not in data[dwarfHatColor]:
        data[dwarfHatColor].update({dwarfName: dwarfPhysics})

    elif dwarfHatColor in data and dwarfName in data[dwarfHatColor] and dwarfPhysics > data[dwarfHatColor][dwarfName]:
        data[dwarfHatColor][dwarfName] = dwarfPhysics


print(data)

for key, val in sorted(data.items(), key=lambda x: ([-i for i in x[1].values()], len([i for i in x[0].values()]))):
    for name, phisic in val.items():
        print(f'({key}) {name} <-> {phisic}')
