# OOП (polymorphism)
# method override; operator overloading
# isinstance(объект, тип) -> True
# isinstance(объект, (тип1,  тип 2, тип N)) -> True
from idlelib.configdialog import is_int

lst = list(range(1, 15))
lst += ['a']

class Stat:
    def __init__(self, vals):
        self.values = vals[:]  # получаем копию

    def is_all_int(self) -> bool:
        return all(isinstance(item, int) for item in self.values)

    def get_min(self):
        if self.is_all_int():
            return min(self.values)
        return None

    def get_max(self):
        if self.is_all_int():
            return max(self.values)
        return None

    def get_aver(self):
        if self.is_all_int():
            return sum(self.values) / len(self.values)
        return None


s = Stat(lst)
print(s.get_min())
print(s.get_max())
print(s.get_aver())

# class Selector:
#     def __init__(self, vals):
#         self.values = vals[:]  # получаем копию
#
#     def get_odd(self):
#         return [x for x in self.values if x % 2 == 1]
#
#     def get_even(self):
#         return [x for x in self.values if x % 2 == 0]
#
#
# s = Selector(lst)
# print(s.get_odd())
# print(s.get_even())
# print(lst)

# from lib import Student, Employee, Person
#
# people = [
#     Person('Александр', 27),
#     Student('Дмитрий', 'ГУАП'),
#     Employee('Пётр', 'Авангард'),
# ]
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_univercity())
#     elif isinstance(person, Employee):
#         print(person.get_company())
#     else:
#         print(person.get_name())

# from lib import Circle, Rectangle, Square
#
# # def shape_info(shape: object):
# #     print(f'Площадь {shape.get_name()}а: {shape.area()}, Периметр: {shape.perimetr()}')
# rect, c, sqr = 'прямоугольник', 'круг', 'квадрат'
#
#
# def shape_info(shape: object):
#     if isinstance(shape, Circle):
#         fig = c
#     elif isinstance(shape, Rectangle):
#         fig = rect
#     elif isinstance(shape, Square):
#         fig = sqr
#     print(f'Площадь {fig}а: {shape.area()}, Периметр: {shape.perimetr()}')
#
#
# s = Square(10)
# shape_info(s)
#
# cr = Circle(10)
# shape_info(cr)
#
# r = Rectangle(5, 2)
# shape_info(r)

# print(dir(s))
# print(dir(cr))

# from lib import Book
#
# book = Book('Язык С++', 'Бьярн Страупструп')
#
# print(f'{book.get_title(), book.get_author()}')

# print(1 + 2)
# print(1 + 2.0)
# print('abc' + 'def')
# print([1, 2] + [3, 4])
#
# def func(x, y):
#     return x + y
#
# print(func(2, 3.0))
