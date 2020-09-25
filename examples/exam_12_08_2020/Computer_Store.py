total_order = 0
discount = 0

while True:
    line = input()
    if line == 'special':
        discount += (total_order + total_order * 0.2) * 0.1
        break

    if line == 'regular':
        break

    line = float(line)
    if line < 0:
        print('Invalid price!')
    else:
        total_order += line


if total_order == 0:
    print('Invalid order!')
else:
    taxes = total_order * 0.2
    total = total_order + taxes
    if discount > 0:
        total -= discount
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_order:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total:.2f}$')