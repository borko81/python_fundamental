shelf_with_books = input().split('&')


def add_book(book, shelf_with_books):
    if book not in shelf_with_books:
        shelf_with_books.insert(0, book)


def take_book(book, shelf_with_books):
    if book in shelf_with_books:
        my_index = shelf_with_books.index(book)
        shelf_with_books.pop(my_index)


def swap_books(one, two, shelf_with_books):
    if one in shelf_with_books and two in shelf_with_books:
        pos_for_book_one = shelf_with_books.index(one)
        pos_for_book_two = shelf_with_books.index(two)
        shelf_with_books[pos_for_book_one], shelf_with_books[pos_for_book_two] = shelf_with_books[pos_for_book_two], shelf_with_books[pos_for_book_one]


def insert_book(book_name, shelf_with_books):
    shelf_with_books.append(book_name)


def check_for_book(index, shelf_with_books):
    print(shelf_with_books[index])


while True:
    common = input().split(' | ')
    if common[0] == 'Done':
        break

    if common[0] == 'Add Book':
        book_name = common[1]
        add_book(book_name, shelf_with_books)

    if common[0] == 'Take Book':
        book_name = common[1]
        take_book(book_name, shelf_with_books)

    if common[0] == 'Swap Books':
        book_one = common[1]
        book_two = common[2]
        swap_books(book_one, book_two, shelf_with_books)

    if common[0] == 'Insert Book':
        book_name = common[1]
        insert_book(book_name, shelf_with_books)

    if common[0] == 'Check Book':
        index = int(common[1])
        if 0 <= index < len(shelf_with_books):
            check_for_book(index, shelf_with_books)


print(', '.join(shelf_with_books))