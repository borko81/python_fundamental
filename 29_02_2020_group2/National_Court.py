employee = 3
count = 0


def calculate_total_time():
    total_emp_work = 0
    for _ in range(employee):
        total_emp_work += int(input())
    return total_emp_work


def check_cigarete_pause(check):
    global count
    count += 1
    if count % check == 0:
        count += 1
    return count



total_emp_work = calculate_total_time()
total_people = int(input())


while True:
    if total_people <= 0:
        break

    check_cigarete_pause(4)
    total_people -= total_emp_work


print(f'Time needed: {count}h.')
