neighborhood = [int(x) for x in input().split('@')]
dec = 2
start = 0


def check(neighborhood, position, start):
    start += position
    if start >= len(neighborhood):
        start = 0

    if neighborhood[start] == 0:
        print(f'Place {start} already had Valentine\'s day.')
    else:
        neighborhood[start] -= 2
        if neighborhood[start] == 0:
            print(f'Place {start} has Valentine\'s day.')
    return neighborhood, start


while True:
    command = input().split()
    if command[0] == 'Love!':
        break

    _, position = command
    position = int(position)
    neighborhood, start = check(neighborhood, position, start)

print(f'Cupid\'s last position was {start}.')
if all(i == 0 for i in neighborhood):
    print('Mission was successful.')
else:
    unhapy = len([i for i in neighborhood if i != 0])
    print(f'Cupid has failed {unhapy} places.')

#print(neighborhood)