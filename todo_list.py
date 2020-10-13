'''
You will receive a todo-notes until you get the command "End". The notes will be in the format:
"{importance}-{value}".
Return the list of todo-notes sorted by importance. The maximum importance will be 10
'''

todos = dict()

while True:
    command = input().split('-')
    if command[0] == 'End':
        print([todos[i] for i in sorted(todos)])
        break

    else:
        importance, name = command
        todos[importance] = name


