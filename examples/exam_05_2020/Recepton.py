f_employee = int(input())
s_employee = int(input())
l_employee = int(input())

students = int(input())
total_per_hour = f_employee + s_employee + l_employee

total = 0
hour = 0

while True:
    if total >= students:
        break
    total += total_per_hour
    hour += 1
    if hour % 4 == 0:
        hour += 1

print(f'Time needed: {hour}h.')
