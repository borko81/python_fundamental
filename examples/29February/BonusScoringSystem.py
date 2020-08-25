'''Create a program that calculates bonus points for each student, for a certain course. On the first line, you are
going to receive the count of the students for this course. On the second line, you will receive the count
of the lectures in the course. Every course has an additional bonus. You are going to receive it on the third line.
On the next lines, you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
Find the student with the maximum bonus and print him/her, along with his attendances in the following format:
"Max Bonus: {maxBonusPoints}."
"The student has attended {studentAttendances} lectures."
Round the bonus points at the end to the nearest bigger number.'''

import math

student_count = int(input())
lecture_count = int(input())
initial_bonus = float(input())

students = []
student_score = {}
max_bonus = 0
max_result_for_student = 0

for i in range(student_count):
    attendances = int(input())
    students.append(attendances)


for i in students:
    total_bonus = i / lecture_count * (5+initial_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_result_for_student = i


print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_result_for_student} lectures.')
