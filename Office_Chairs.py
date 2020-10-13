num = int(input())

all = 0

for _ in range(1, num + 1):
    chairs, taken = input().split()
    len_chairs = len(chairs)
    taken = int(taken)
    if taken > len_chairs:
        print(f'{taken-len_chairs} more chairs needed in room {_}')
    else:
        all += 1

if all == num:
    print(f'Game On, {all} free chairs left')