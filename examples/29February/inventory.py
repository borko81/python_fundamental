'''
You will receive a journal with some Collecting items, separated with ', ' (comma and space). After that, until
receiving "Craft!" you will be receiving different commands.
Commands (split by " - "):
    • "Collect - {item}" – Receiving this command, you should add the given item in your inventory. If the item already
        exists, you should skip this line.
    • "Drop - {item}" – You should remove the item from your inventory, if it exists.
    • "Combine Items - {oldItem}:{newItem}" – You should check if the old item exists, if so, add the new item after
        the old one. Otherwise, ignore the command.
    • "Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
'''


collections = input().split(', ')

while True:
    craft = input()
    if craft == 'Craft!':
        print(', '.join(collections))
        break

    if craft.startswith('Collect'):
        _, item = craft.split(' - ')
        if item not in collections:
            collections.append(item)

    if craft.startswith('Drop'):
        _, item = craft.split(' - ')
        if item in collections:
            collections.remove(item)

    if craft.startswith('Combine Items'):
        _, items = craft.split(' - ')
        old_item, new_item  = items.split(':')
        if old_item in collections:
            position = collections.index(old_item)
            collections.insert(position + 1, new_item)

    if craft.startswith('Renew'):
        _, item = craft.split(' - ')
        if item in collections:
            i = collections.pop(collections.index(item))
            collections.append(i)

