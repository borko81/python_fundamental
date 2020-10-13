list_of_emp_happines = [int(x) for x in input().split()]
happines = int(input())

list_of_emp_happines = [x * happines for x in list_of_emp_happines]
average_happines = sum(list_of_emp_happines) / len(list_of_emp_happines)

result = len([i for i in list_of_emp_happines if i >= average_happines])

if result >= len(list_of_emp_happines) // 2:
    print(f'Score {result}/{len(list_of_emp_happines)}. Employees are happy!')
else:
    print(f'Score {result}/{len(list_of_emp_happines)}. Employees are not happy!')