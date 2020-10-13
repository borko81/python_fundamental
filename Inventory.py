items = input().split(', ')


def craft(items, item):
    if item not in items:
        items.append(item)
    return items


def drop(items, item):
    if item in items:
        items.remove(item)
    return items


def combine_item(items, old_item, new_item):
    if old_item in items:
        posiiton = items.index(old_item)
        items.insert(posiiton + 1, new_item)
    return items


def renew(items, item):
    if item in items:
        pos = items.index(item)
        temp = items.pop(pos)
        items.append(temp)
    return items


while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        break

    elif command[0] == 'Collect':
        _, item = command
        items = craft(items, item)

    elif command[0] == 'Drop':
        _, item = command
        items = drop(items, item)

    elif command[0] == 'Combine Items':
        _, item = command
        old_item, new_item = item.split(':')
        items = combine_item(items, old_item, new_item)

    elif command[0] == 'Renew':
        _, item = command
        items = renew(items, item)


print(", ".join(items))