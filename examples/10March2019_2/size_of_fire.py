'''Create a program that calculates the water that is needed to put out a "fire cell", based on the given
information about its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the
needed water to put out the fire.  They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each
of the fire types, and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.
Type of Fire
Range

High 81 - 125
Medium 51 - 80
Low 1 - 50

If a cell is valid, you have to put it out by reducing the water with its value. Putting out fire also takes effort
and you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the total
effort. Keep putting out cells until you run out of water. If you don’t have enough water to put out a given
cell – skip it and try the next one. In the end, print the cells you have put out in the following format:'''

fire_ceils = input().split('#')
water = int(input())

given_fire = []
effort = 0


def calc_me(value):
        global water
        global effort
        given_fire.append(value)
        water -= value
        effort += value * 0.25


for fire in fire_ceils:
    size, value = fire.split(' = ')
    value = int(value)

    if size == 'High' and 81 <= value <= 125 and water >= value:
        calc_me(value)

    elif size == 'Medium' and 51 <= value <= 80  and water >= value:
        calc_me(value)

    elif size == 'Low' and 1 <= value <= 50  and water >= value:
        calc_me(value)


print('Cells:')
for v in given_fire:
    print(f' - {v}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(given_fire)}')

