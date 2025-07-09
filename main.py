# OOП (encapsulation)
# Методы классов и анализ предыдущих вызовов
# Конструктор
from lib import Car

car = Car('Skoda', 'Octavia', 'red')
car.start_engine()
# car.engine_on = True
car.drive_to('город')

car2 = Car()
car2.start_engine()
car2.drive_to('город')

# Методы классов
# class Greater:
#     def hello(self, name='Noname') -> None:
#         print('Привет,', name)
#
#     def goodbye(self):
#         print('Пока')
#
#
# g = Greater()
# g.hello('Ольга')
# g.goodbye()
#
# g2 = Greater()
# g2.hello()
# g2.goodbye()

# Свойства классов
# class Fruit:
#     pass
#
#
# a = Fruit()
# b = Fruit()
# c = Fruit()
#
# a.name = 'Яблоко'
# a.weight = 120
# b.name = 'Груша'
# b.weight = 150
#
# print(a.name)
# print(c.weight)

# Регулярные выражения (поиск по паттерну)
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз m более
# {,n} - не более n раз
# {m,n} - от m до n (без пробела)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности (32767) {0,}
# + - от 1 до бесконечности (32767) {1,}
# https://regex101.com

# import re
# import requests
#
# pattern = r'<img[^>]+src="([^">]+)"'
# # Сначала проверили
# # test_string = '<img height="50" width="150" src="images/bg.jpg">'
# html = requests.get('https://yandex.ru').text
# result = re.findall(pattern, html)
# print(result)


# pattern = r'\b\w{4}\b' # все слова из 4 символов
# pattern = r'\d' # все цифры от 0 до 9
# pattern = r'\d{3}'  # три цифры подряд
# pattern = r'начало!\Z' # на что заканчивается
# pattern = '[0-5][0-9]' # две идущие подряд
# pattern = '[а-яА-я]' # все буквы от а до я и от А до Я
# pattern = '[^ерм]'  # исключить символы
# pattern = r'\((.+?)\)' # вытащить текст из скобок
# pattern = 'Go{2,}gle' # Google где 2 и более o
# pattern = r'стеклянн?ый' # 2-я "н" может присутствовать
# "жадный" и "ленивый" квантификатор (greedy quantifier)
# pattern = r'<img.*>' # жадный квантификатор
# pattern = r'<img.*?>' # ленивый (lazy, non-greedy) квантификатор
# pattern = r'<img[^>]+src="([^">]+)"' # только путь к картинке
# pattern = r'<p>(.*?)</p>' # содержимое абзаца html
# pattern = r'<p[^>]*>(.*?)</p>' # содержимое абзаца html c атрибутами
# Убираем все знаки препинания
# def remove_punctuation(input_str: str) -> str:
#     """
#     Методом sub() заменяем все найденные совпадения
#     пустой строкой и возвращаем "очищенную"
#     :param input_str: строка со знаками препинания
#     :return: строку, очищенную от зн. преп.
#     """
#     return re.sub(r'[^\w\s]', '', input_str)

# Split()
# test_string = '   яблоко,  груша.   банан  ; слива !  абрикос  '
# # test_string = ''.join(test_string.split())  # убрали все пробелы
# result = re.split(pattern, test_string)
# # через map
# # result = list(map(lambda x: x.strip(), result))
# # через list comprehension с сортировкой
# result = sorted(x.strip() for x in result)
# print(result)
