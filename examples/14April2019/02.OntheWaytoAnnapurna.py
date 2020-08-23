'''Create a program, that lists stores and the items that can be found in them. You are going to be receiving commands
with the information you need until you get the "End" command. There are three possible commands:
    • "Add->{Store}->{Item}"
        ◦ Add the store and the item in your diary. If the store already exists, add just the item.
    • "Add->{Store}->{Item},{Item1}…,{ItemN}"
        ◦ Add the store and the items to your notes. If the store already exists in the diary – add just the items to it.
    • "Remove->{Store}"
        ◦ Remove the store and its items from your diary, if it exists.
In the end, print the collection sorted by the count of the items in descending order and then by the names of the
stores, again, in descending order in the following format:
Stores list:
{Store}
<<{Item}>>
<<{Item}>>
<<{Item}>>'''

diary = {}

while True:
    line = input()
    if line == 'END':
        break

    if line.startswith('Add'):
        _, store, items = line.split('->')

        if store in diary:
            if len(items.split(',')) > 1:
                items = items.split(',')
                diary[store].extend(items)
            else:
                diary[store].append(items)
        else:
            if len(items.split(',')) > 1:
                items = items.split(',')
                diary[store] = items
            else:
                diary[store] = [items]

    elif line.startswith('Remove'):
        _, store = line.split('->')
        try:
            del diary[store]
        except:
            pass



print('Stores list:')

for store, items in sorted(diary.items(), key=lambda x: (len(x[1]), x[0]), reverse=True):
    print(f'{store}')
    for i in items:
        print(f'<<{i}>>')