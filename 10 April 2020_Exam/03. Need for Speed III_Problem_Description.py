number_of_lines = int(input())

car_data = {}

for _ in range(number_of_lines):
    car_info = input()
    name, milieage, fuel_available = car_info.split('|')
    milieage = int(milieage)
    fuel_available = int(fuel_available)

    if not name in car_data:
        car_data[name] = [0.00, 0.00]
    car_data[name][0] = milieage
    car_data[name][1] = fuel_available

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(' : ')

    if command[0] == 'Drive':
        car, distance, fuel = command[1:]
        distance = int(distance)
        fuel = int(fuel)

        if fuel > car_data[car][1]:
            print("Not enough fuel to make that ride")

        elif fuel <= car_data[car][1]:
            car_data[car][0] += distance
            car_data[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if car_data[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del car_data[car]

    elif command[0] == 'Refuel':
        car, fuel = command[1:]
        fuel = int(fuel)
        if fuel + car_data[car][1] < 75:
            car_data[car][1] += fuel
        else:
            fuel = 75 - car_data[car][1]
            car_data[car][1] = 75

        print(f"{car} refueled with {fuel} liters")


    elif command[0] == 'Revert':
        car, kilometers = command[1:]
        kilometers = int(kilometers)

        car_data[car][0] -= kilometers

        if car_data[car][0] < 10000:
            car_data[car][0] = 10000

        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in sorted(car_data.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")

"""
On the first line of the standard input you will receive an integer n – the number of cars that you can obtain. On the next n lines the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
{car}|{mileage}|{fuel}
Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
    • Drive : {car} : {distance} : {fuel} 
        ◦ You need to drive the given distance and you will need the given fuel to do that. If the car doesn`t have enough fuel print:
"Not enough fuel to make that ride"
        ◦ If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel and print: 
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
        ◦ You like driving new cars only, so if the mileage of a car reaches 100 000 km, remove it from the collection(s). Print:
"Time to sell the {car}!"
    • Refuel : {car} : {fuel}
        ◦ Refill the tank of your car. 
        ◦ Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up. 
        ◦ Print a message in the following format:
"{car} refueled with {fuel} liters"
    • Revert : {car} : {kilometers}
        ◦ Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
"{car} mileage decreased by {amount reverted} kilometers"
        ◦ If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and 
DO NOT print anything.
Upon receiving the "Stop" command you need to print all cars in your possession, sorted by their mileage in decscending order, then by their name in ascending order, in the following format:
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."""
