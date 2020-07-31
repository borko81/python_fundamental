# 02. Judge

contest_word = {}
count = 1
user_result = {}

while True:
    line = input()
    if line == 'no more time':
        break

    username, contest, points = line.split(' -> ')
    points = int(points)

    if contest not in contest_word:
        contest_word[contest] = {username: points}

    elif contest in contest_word:
        if username in contest_word[contest] and contest_word[contest][username] < points:
            contest_word[contest][username] = points

        elif username not in contest_word[contest]:
            contest_word[contest].update({username: points})


for constestName, participants in contest_word.items():
    print(f'{constestName}: {len(participants)} participants')

    for username, point in sorted(participants.items(), key=lambda x: (-x[1], x[0])):
        print(f'{count}. {username} <::> {point}')
        if username not in user_result:
            user_result[username] = point
        else:
            user_result[username] += point
        count += 1
    count = 1

print('Individual standings:')

for name, point in sorted(user_result.items(), key=lambda x: (-x[1], x[0])):
    print(f'{count}. {name} -> {point}')
    count += 1