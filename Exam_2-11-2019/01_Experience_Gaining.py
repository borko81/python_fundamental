needed_experience = float(input())
count_fo_battle = int(input())
gain_exp = 0
WIN = False

for i in range(1, count_fo_battle + 1):
    exp = float(input())

    if i % 3 == 0:
        exp = exp + exp * 0.15

    if i % 5 == 0:
        exp = exp - exp * 0.10

    gain_exp += exp

    if gain_exp >= needed_experience:
        print(f'Player successfully collected his needed experience for {i} battles.')
        WIN = True
        break

if not WIN:
    neededExperience = needed_experience - gain_exp
    print(f'Player was not able to collect the needed experience, {neededExperience:.2f} more needed.')