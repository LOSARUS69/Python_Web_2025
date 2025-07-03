# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>: <выражение>
# потоковый ввод sys.stdin (Ctrl + D)
import sys

data = [d.strip('\n') for d in sys.stdin.readlines()]

temp = [] # индекс строки в data и число слов в виде кортежей
for i, s in enumerate(data):
    temp.append((i, len(s.split())))

temp.sort(key=lambda x:x[1])

index = temp[0][0]
res = sorted(data[index].split())

print(*res, sep='-')


# any - любой элемент коллекции вернул True
# all - все элементы коллекции вернули True

# print(all([1, 2, 3]))  # все элементы ненулевые
# print(all([1, 2, 0]))  # один элемент нулевой
# print(all([1]))
#
# words = 'один два три'.split() # > 3
# list_for_analize = list(map(lambda x: len(x) > 2, words))
# print(any(list(map(lambda x: len(x) > 5, words))))

# fruits = ['ананас', 'банан', 'ежевика', 'арбуз', 'малина']
#
# # print(sorted(fruits, key=lambda s: (len(s), s[-1])))
#
# goods = [
#     ['Утюг', 1000, 2],
#     ['Фен', 1000, 5],
#     ['Телевизор', 8000, 3]
# ]

# print(sorted(goods, key=lambda s: (s[1], s[2], s[0])))

# numbers = [1, 2, 3, 4, 5]  # list(range(1, 6)
# squares = {n: n ** 2 for n in numbers}
# print(squares)
#
# squares = {n: n ** 2 for n in range(1, 10) if n % 2 == 0}
# print(squares)
#
# source_dict = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# dest_dict = {k: v * 2 for k, v in source_dict.items()}
# print(dest_dict)

# fruits = ['ананас', 'банан', 'ежевика', 'малина', 'арбуз']
#
# print(sorted(fruits, key=lambda ch: len(ch)))


# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
#        set([x.upper() for x in ENGLISH_ABC]) ^
#        set([x.upper() for x in RUSSIAN_ABC]))
# # print(ABC)
# # print(ENGLISH_ABC)
# # print(RUSSIAN_ABC)
# txt = ('Я знаю, что я ничего не знаю. '
#        'Но другие не знают и этого. А значит, я знаю больше, чем они.')
#
# d = {}
#
#
# def remove_punctuation(text):
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, text))
#
#
# def get_words(text: str) -> list:
#     return remove_punctuation(text).split()
#
#
# def long_words(text, length=4) -> filter:
#     return filter(lambda word: len(word) >= length, get_words(text))
#
#
# words = get_words(txt.lower())
#
# # Считаем частоту слов
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
#
# res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
#
# for k, v in res.items():
#     print(k, v)

# print(list(long_words(txt)))

# Функция критерия отбора элементов списка
# Критерий: длина слова
# def is_longer_six(word):
#     return len(word) > 6

# is_longer_six = lambda word: len(word) > 6


# Критерий - первая буква
# def is_first_letter_a(word):
#     return word[0] == 'а'

# is_first_letter_a = lambda word: word[0] == 'а'

# Критерий - вхождение подстроки
# в частности 'ан'
# def string_contains(s):
#     return 'ан' in s

# string_contains = lambda s: 'ан' in s

# print(string_contains('банан'))
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # -> 123456789
# res = ''.join(map(str, nums))
# print(res)
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#          'длина', 'которых', 'больше', 'шести']
#
# fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']
#
# result = list(filter(lambda word: len(word) > 6, words))
# print(result)
#
# res = list(filter(lambda x: x[0] == 'а', fruits))
# print(res)
#
# res = list(filter(lambda s: 'ан' in s, fruits))
# print(res)
#
# # в одну строку вывести список квадратов чисел от 3 до 15
# # [9, 16, 25.....]
# # res = list(map(lambda y: y ** 2, range(3, 16)))
# res = [y ** 2 for y in range(3, 16)]
# print(res)
#
# long_words = [word for word in words if len(word) > 6]
# print(long_words)
