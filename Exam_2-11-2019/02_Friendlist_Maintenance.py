friend = input().split(', ')


def blacklist(search_name, f_list):
    if search_name not in f_list:
        print(f'{search_name} was not found.')
    else:
        myindex = f_list.index(search_name)
        f_list[myindex] = 'Blacklisted'
        print(f'{search_name} was blacklisted.')


def error(search_index, f_list):
    if search_index in range(len(f_list)):
        temp = f_list[search_index]
        if temp not in 'Blacklisted Lost'.split():
            print(f'{f_list[search_index]} was lost due to an error.')
            f_list[search_index] = 'Lost'


def change(s_index, new_name ,f_list):
    if s_index in range(len(f_list)):
        temp = friend[s_index]
        friend[s_index] = new_name
        print(f'{temp} changed his username to {new_name}.')


while True:
    command = input().split()
    if command[0] == 'Report':
        print(f"Blacklisted names: {friend.count('Blacklisted')}")
        print(f"Lost names: {friend.count('Lost')}")
        print(" ".join(friend))
        break

    elif command[0] == 'Blacklist':
        _, name = command
        blacklist(name, friend)

    elif command[0] == 'Error':
        _, index = command
        index = int(index)
        error(index, friend)

    elif command[0] == 'Change':
        _, index, new_name = command
        index = int(index)
        change(index, new_name, friend)
