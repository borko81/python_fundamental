people_waiting = int(input())
state = [int(x) for x in input().split()]

max_people = 4
result = []
temp = people_waiting


for i in state:
    a = people_waiting - (max_people - i)
    if a == 0:
        result.append(max_people - i)
        people_waiting -= (max_people - i)
        break
    elif a > 0:
        result.append(max_people - i)
        people_waiting -= (max_people - i)
    elif a < 0:
        result.append(people_waiting - i)
        people_waiting = 0
        break


for i, v  in enumerate(result):
    state[i] += v


if people_waiting == 0 and any(i!=max_people for i in state):
    print('The lift has empty spots!')
    for p in state:
        print(p, end = ' ')
if people_waiting == 0 and all(i==max_people for i in state):
    for p in state:
        print(p, end = ' ')
elif people_waiting > 0:
    print(f'There isn\'t enough space! {people_waiting} people in a queue!')
    for p in state:
        print(p, end = ' ')
