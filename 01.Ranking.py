# 01. Ranking
con_pass = {}
users = {}
max_result = {}

while True:
    line = input()
    if line == 'end of contests':
        break
    contest, password = line.split(':')
    if contest not in con_pass:
        con_pass[contest] = password

while True:
    line = input()
    if line == 'end of submissions':
        break
    contest, password, username, points = line.split('=>')
    points = int(points)

    if contest in con_pass:
        if con_pass[contest] == password:
            if username not in users:
                users[username] = {contest: points}

            elif username in users and contest in users[username]:
                if users[username][contest] <= points:
                    users[username][contest] = points

            elif username in users and contest not in users[username]:
                users[username].update({contest: points})


for k, v in users.items():
    for r in v:
        if k not in max_result:
            max_result[k] = v[r]
        else:
            max_result[k] += v[r]


user, points = sorted(max_result.items(), key=lambda x: -x[1])[0]

print(f'Best candidate is {user} with total {points} points.')
print('Ranking:')

for name, score in sorted(users.items()):
    print(name)
    for n, s in sorted(score.items(), key=lambda x: -x[1]):
        print(f'#  {n} -> {s}')















