# 03. MOBA Challenger
users = {}

while True:
    line = input()
    if line == 'Season end':
        break

    if ' vs ' in line:
        player_one, player_two = line.split(' vs ')
        # Проверка дали двамата потребителя ги има в дикшинарито
        if player_one in users and player_two in users:
            for p1 in users[player_one]:
                for p2 in users[player_two]:
                    # Проверка дали двамата потребителя имат еднакви склилове за турнир
                    if p1 == p2:
                        if users[player_one][p1] == users[player_two][p1]:
                            continue

                        elif users[player_one][p1] > users[player_two][p1]:
                            users[player_two][p1] = 0

                        elif users[player_one][p1] < users[player_two][p1]:
                            users[player_one][p1] = 0

    elif ' -> ' in line:
        player, position, skill = line.split(' -> ')
        skill = int(skill)
        # Дали потребителя го има на масата
        if player not in users:
            users[player] = {position: skill}

        # Дали потребителя го има на масата и ако да дали скила е по-малък от новият
        elif player in users and position in users[player] and skill > users[player][position]:
            users[player][position] = skill

        # Тука май бъркам нещо
        elif player in users and position not in users[player]:
            users[player].update({position: skill})


new_users = {}
for k, v in users.items():
    new_users[k] = {i:s for i, s in v.items() if s != 0}

# Result
for player, totalSkill in sorted(new_users.items(), key=lambda x: (-sum(i for i in x[1].values()), x[0])):
    if len(new_users[player]) == 0:
        continue
    else:
        print(f'{player}: {sum(totalSkill.values())} skill')
    for user, skill in sorted(new_users[player].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {user} <::> {skill}')