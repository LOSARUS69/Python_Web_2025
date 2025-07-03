# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>: <выражение>


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

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # -> 123456789
res = ''.join(map(str, nums))
print(res)

words = ['В', 'этом', 'списке', 'останутся', 'слова',
         'длина', 'которых', 'больше', 'шести']

fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']

result = list(filter(lambda word: len(word) > 6, words))
print(result)

res = list(filter(lambda x: x[0] == 'а', fruits))
print(res)

res = list(filter(lambda s: 'ан' in s, fruits))
print(res)

# в одну строку вывести список квадратов чисел от 3 до 15
# [9, 16, 25.....]
# res = list(map(lambda y: y ** 2, range(3, 16)))
res = [y ** 2 for y in range(3, 16)]
print(res)

long_words = [word for word in words if len(word) > 6]
print(long_words)
