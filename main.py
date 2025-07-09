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

import re

# pattern = r'\b\w{4}\b' # все слова из 4 символов
# pattern = r'\d' # все цифры от 0 до 9
# pattern = r'\d{3}'  # три цифры подряд
# pattern = r'начало!\Z' # на что заканчивается
# pattern = '[0-5][0-9]' # две идущие подряд
# pattern = '[а-яА-я]' # все буквы от а до я и от А до Я
# pattern = '[^ерм]'  # исключить символы
# pattern = r'\((.+?)\)' # вытащить текст из скобок
pattern = 'Go{2,}gle' # Google где 2 и более o
test_string = 'Google, Gooogle, Gooooooogle'

result = re.findall(pattern, test_string)
print(result)
