# 01. Storage


# class Storage:
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#
#     def add_product(self, product):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#
#     def get_products(self):
#         return self.storage

# 02. Weapon

# class Weapon:
#
#     def __init__(self, bullets: int):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return f'shooting...'
#         else:
#             return f'no bullets left'
#
#     def __repr__(self):
#         return f'Remaining bullets: {self.bullets}'

# 03. Catalogue


# class Catalogue:
#
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def get_by_letter(self, first_letter):
#         return [i for i in self.products if i.startswith(first_letter)]
#
#     def __repr__(self):
#         r = ''
#         r += f'Items in the {self.name} catalogue:\n'
#         r += f'\n'.join(sorted(self.products))
#         return r

# 04. Town


# class Town:
#
#     def __init__(self, name):
#         self.name = name
#         self.latitude = None
#         self.longitude = None
#
#     def set_latitude(self, latitude):
#         self.latitude = latitude
#
#     def set_longitude(self, longitude):
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'


# 05. Class

# class Class:
#     __students_count = 22
#
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#         self.grades = []
#
#     def add_student(self, name, grade):
#         if Class.__students_count > 0:
#             self.students.append(name)
#             self.grades.append(grade)
#             Class.__students_count -= 1
#
#     def get_average_grade(self):
#         return round(sum(self.grades) / len(self.grades), 2)
#
#     def __repr__(self):
#         return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {self.get_average_grade()}'

# 06. Inventory


# class Inventory:
#
#     def __init__(self, capacity):
#         self.__capacity = capacity
#         self.items = []
#
#     def add_item(self, item):
#         if len(self.items) >= self.__capacity:
#             return f'not enough room in the inventory'
#         else:
#             self.items.append(item)
#
#     def get_capacity(self):
#         return len(self.items)
#
#     def __repr__(self):
#         return f'Items: {", ".join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}'

# 07. Articles

# class Article:
#
#     def __init__(self, title, content, author):
#         self.author = author
#         self.content = content
#         self.title = title
#
#     def edit(self, new_content):
#         self.content = new_content
#
#     def change_author(self, new_author):
#         self.author = new_author
#
#     def rename(self, new_title):
#         self.title = new_title
#
#     def __repr__(self):
#         return f'{self.title} - {self.content}: {self.author}'

# 08. Vehicle


# class Vehicle:
#
#     def __init__(self, type, model, price):
#         self.price = price
#         self.model = model
#         self.type = type
#         self.owner = None
#
#     def buy(self, money, owner):
#         if money >= self.price and self.owner is None:
#             self.owner = owner
#             return f'Successfully bought a {self.type}. Change: {(money-self.price):.2f}'
#         elif money < self.price:
#             return f'Sorry, not enough money'
#
#         elif self.owner is not None:
#             return f'Car already sold'
#
#     def sell(self):
#         if self.owner is not None:
#             self.owner = None
#         else:
#             return f'Vehicle has no owner'
#
#     def __repr__(self):
#         if self.owner is not None:
#             return f'{self.model} {self.type} is owned by: {self.owner}'
#         else:
#             return f'{self.model} {self.type} is on sale: {self.price}'

# 09. Movie


# class Movie:
#
#     __watched_movies = 0
#
#     def __init__(self, name, director):
#         self.director = director
#         self.name = name
#         self.watched = False
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def change_director(self, new_director):
#         self.director = new_director
#
#     def watch(self):
#         if self.watched is False:
#             self.watched = True
#             Movie.__watched_movies += 1
#
#     def __repr__(self):
#         return f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}'











































