# OOП (encapsulation)
# задачи
from lib import Balance

WELCOME = """
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *  Добро пожаловать в демонстрацию возможностей весов «Баланс-0.1»! *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    Вы можете добавлять вес в произвольных единицах на левую или правую чашу.
        Для этого введите команду вида "X вес", где X - это указатель чаши, а вес - это число.
        Для левой чаши используются указатели: Л, L, S
        Для правой чаши используются указатели: П, R, D
        Текущая версия программы поддерживает только целочисленный ввод
        Контроль консистентности единиц ввода на вашей ответственности.
        Мы предполагаем, что все здесь взрослые люди.
    Команды для вывода результата:
        ? - выводит сообщение о текущем балансе весов
        ?+ - сообщает, на сколько больше веса в какой чаше
        ?* - сообщает, насколько больше веса в какой чаше
        ?? - выводит вес на обеих чашах
    Для сброса и обнуления обеих чаш весов наберите команду "000"
    Для завершения работы наберите команду "---"
"""
LEFT_TRIGGERS = 'ЛLSKЫДCС'
RIGHT_TRIGGERS = 'ПRDGКВЗPР'


def main():
    balance = Balance()

    print(WELCOME)
    while (command := input('> ').strip().upper()) != "---":
        if command == "000":
            print(balance.reset())

        elif command == "?":
            print(balance.result())

        elif command == "??":
            print(balance.get_status())

        elif command == "?+":
            difference = balance.get_difference()
            print('на чашах одинаково веса' if difference == 0 else \
                      f'левая чаша тяжелее на {difference}' if difference > 0 else \
                          f'правая чаша тяжелее на {-difference}')

        elif command == "?*":
            relative_difference = balance.get_difference_percentage()
            print('никакая чаша не тяжелее' if relative_difference == 0 else \
                      f'левая чаша тяжелее на {relative_difference:3.2f}% от правой' if relative_difference > 0 else \
                          f'правая чаша тяжелее на {-relative_difference:3.2f}% от левой')

        elif len(command) <= 1:
            print('неверная команда')

        else:
            try:
                key = command[0]
                value = int(command[1:].strip())
                if key in LEFT_TRIGGERS:
                    balance.add_left(value)
                elif key in RIGHT_TRIGGERS:
                    balance.add_right(value)
                else:
                    print('неверная команда')
            except ValueError as ex:
                print('ошибка ввода:', ex)

    print('Спасибо за интерес к взвешиванию!')

main()

# from lib import Separator
#
# s = Separator()
#
# for i in range(20):
#     s.add_num(i)
#
# print(s.get_even())

# cl = Clicker()
#
# cl.click()
# cl.click()
# cl.click()
#
# print(cl.get_counter())
# cl.reset()
# print(cl.get_counter())

# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# print('В парке машин:', Car.get_counter())

# from lib import Person
#
# p = Person()
# p.set_age(7897)
# print(p.get_name())
# p.person_info()

# from lib import Car
#
# car = Car('Skoda', 'Octavia', 'red')
# car.start_engine()
# # car.engine_on = True
# car.drive_to('город')
#
# car2 = Car()
# car2.start_engine()
# car2.drive_to('город')

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
