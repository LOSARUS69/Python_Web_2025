# Области видимости
PI = 3.1415
# Shadows name 'square' from outer scope
def greet(name):
    print('Привет,', name)
    name = 'друг'
    print('Здравствуй,', name)


def square_area(length: int, width: int) -> None:
    area = length * width
    print(f'Площадь площади = {area}')


def circle_length(radius: float):
    perimetr = 2 * PI * radius
    print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')


def print_array(array: list) -> None:
    for item in array:
        print(item)


# Главная функция
def main():
    area = 'Дворцовая площадь'
    words = ['Привет', 'мир']
    greet('Пётр')
    print('Давай встретимся, где', area)
    square_area(320, 240)
    print('Ну что? Встречаемся, где', area)
    circle_length(5)
    print_array(words)
    print_array(['a', 'b', 'c'])


main()

# Пример как делать не надо
# a = [1, 2]
#
# def change_array():
#     a[0] = 0
#
# change_array()
# print(a)

# # Функция с аннотацией
# num_to_str = {
#     0: 'ноль',
#     1: 'один',
#     2: 'два',
#     3: 'три',
#     4: 'четыре',
#     5: 'пять',
#     6: 'шесть',
#     7: 'семь',
#     8: 'восемь',
#     9: 'девять',
#     10: 'десять',
#     11: 'одиннадцать',
#     12: 'двенадцать',
#     13: 'тринадцать',
#     14: 'четырнадцать',
#     15: 'пятнадцать',
#     16: 'шестнадцать',
#     17: 'семнадцать',
#     18: 'восемнадцать',
#     19: 'девятнадцать',
#     20: 'двадцать',
#     30: 'тридцать',
#     40: 'сорок',
#     50: 'пятьдесят',
#     60: 'шестьдесят',
#     70: 'семьдесят',
#     80: 'восемьдесят',
#     90: 'девяносто'
# }
#
#
# def number_to_words(n: int) -> str:
#     """
#     Функция, принимающая число и возвращающее его словами
#     :param n: двузначное число
#     :return: это число словами
#     """
#     if len(str(n)) > 2:
#         return 'Введите двузначное число'
#     if len(str(n)) == 1 or n in num_to_str:
#         return num_to_str[int(n)]
#     return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]
#
#
# print(number_to_words(33))
