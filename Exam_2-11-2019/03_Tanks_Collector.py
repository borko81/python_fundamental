vehicle = input().split(', ')
row = int(input())


def add_tank(my_vehicle, name):
    if name in my_vehicle:
        print('Tank is already bought')
    else:
        print('Tank successfully bought')
        my_vehicle.append(name)


def remove_tank(my_vehicke, name):
    if name not in my_vehicke:
        print('Tank not found')
    else:
        print('Tank successfully sold')
        del my_vehicke[my_vehicke.index(name)]


def remove_at_tank(my_vehicke, myindex):
    if myindex in range(len(my_vehicke)):
        print('Tank successfully sold')
        del my_vehicke[myindex]
    else:
        print('Index out of range')


def insert_tank(my_vehicke, myindex, name):
    test = myindex not in range(len(my_vehicke))
    if test:
        print('Index out of range')
    elif test is False and name in my_vehicke:
        print('Tank is already bought')
    else:
        print('Tank successfully bought')
        my_vehicke.insert(myindex, name)


for _ in range(row):
    command = input().split(', ')
    if command[0] == 'Add':
        _, tank_name = command
        add_tank(vehicle, tank_name)

    elif command[0] == 'Remove':
        _, tank_name = command
        remove_tank(vehicle, tank_name)

    elif command[0] == 'Remove At':
        _, s_index = command
        s_index = int(s_index)
        remove_at_tank(vehicle, s_index)

    elif command[0] == 'Insert':
        _, s_index, tank_name = command
        s_index = int(s_index)
        insert_tank(vehicle, s_index, tank_name)


print(", ".join(vehicle))