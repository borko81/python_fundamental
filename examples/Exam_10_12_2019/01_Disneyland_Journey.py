cost = float(input())
months_number = int(input())

money = 0

for m in range(1, months_number + 1):

    if m & 1 and m != 1:
        money -= money * 0.16

    if m % 4 == 0:
        money += money * 0.25

    money += cost * 0.25


if money >= cost:
    print(f'Bravo! You can go to Disneyland and you will have {(money - cost):.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {(cost - money):.2f}lv. more.')