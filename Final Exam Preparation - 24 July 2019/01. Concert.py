from collections import defaultdict
band = defaultdict(list)
band_time = defaultdict(int)

while True:
    command = input()
    if command == 'start of concert':
        break

    command = command.split('; ')
    if command[0] == 'Add':
        name_of_band = command[1]
        memebers = command[2].split(', ')
        for m in memebers:
            if m.strip() not in band[name_of_band]:
                band[name_of_band].append(m.strip())

    elif command[0] == 'Play':
        band_name = command[1]
        time = int(command[2])
        band_time[band_name] += time

show_band = input().strip()

total_time = sum(band_time.values())
print(f"Total time: {total_time}")

for name, time in sorted(dict(band_time).items(), key=lambda x: (-x[1], x[0])):
    print(f"{name.strip()} -> {time}")


band = dict(band)


for k, v in band.items():
    if k == show_band:
        print(k.strip())
        for member in v:
            print(f"=> {member.strip()}")


'''
You will read commands until you receive "start of concert" command.
There are two types of commands:
    • "Add; {bandName}; {member 1}, {member 2}, {member 3}" - applies a band and a list of members to the concert. All members must be unique so don't add duplicates. If you receive the same band twice add only those members that aren't present in the list.
    • "Play; {bandName}; {time}" – the band with the given name plays an amount of time on the stage.  If you receive a band that has already applied in the concert, just increase the band time.
If in both commands the band does not exist, add it.
At the end you have to print the total time and the bands ordered by the time on stage in descending order, then by band name in ascending order. 
Also the final input line will be "{bandName}" and you have to print all members for this band in insertion order.'''