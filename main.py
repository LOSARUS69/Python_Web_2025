# Словари
# Пустой словарь
# 1. d = {}
# 2. d = dict()
# Предзаполненный словарь
d = {
    'table': ['таблица', 'стол'],
    'well': ['хорошо', 'колодец'],
    'chair': 'стул',
    'apple': 'яблоко',
    1: 'один',
}

print(d['well'][0])
if type(d['well']) == list:
    d['well'].append('скважина')
d['plum'] = 'слива'
print(d['plum'])
del d['well']

deleted_item = d.pop('apple')

print('Удалился элемент:', deleted_item)

print('Есть ли стул в словаре')
if 'chair' in d:
    print('Да, есть')

for key in d:
    print(key, '->', d[key])

""" Методы словаря   
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
 'pop', 'popitem', 'setdefault', 'update', 'values']
"""


# print(d) # - словарь целиком "как есть"





# N = 3
# matrix = [[i + j for j in range(N)] for i in range(1, 10, 3)]
# print(matrix)

# matrix = []
#
# start = 1
# N = 4
#
# for i in range(N):
#     table = []
#     for j in range(start, start + N):
#         table.append(j)
#     matrix.append(table)
#     start += N
#
# print(matrix)

# N = 3
# # matrix = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9],
# # ]
#
# matrix = [[1] * N for _ in range(N)]
# print(matrix)
# # обход 2-мерного списка (матрицы)
# count = 1
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         matrix[row][col] = count
#         count += 1
# print(matrix)

# text = 'Списочные выражения применяются для эффективности кода'

# res = [a for a in text.split() if (text.index(a) + 1) % 3 == 0]
# res = [a for a in text.split()[2::3]]
# операции со списком
# print(res)

# squares = []
# for i in range(10):
#     squares.append(i ** 2)

# список квадратов чисел
# squares = [i ** 2 for i in range(10)]

# список квадратов чётных чисел
# squares = [i ** 2 for i in range(10) if i % 2 == 0]
# print(*squares, sep=', ')
#
# # произведение i и j
# print([i * j for i in range(3) for j in range(3)])
#
# n = '100 200 300 400 500 600 700 800 900'
# approved = [500, 800]
# a = [int(i) for i in n.split() if int(i) in approved]
# # какие-то действия со списком a
# print(a)

############################################################

# # Фраза: ну?, я типо, вообще: короче, не понимаю этот язык!
# commas = (',', '!', '.', '?', '-', ':')
# stop_words = {'ну', 'типо', 'короче', 'не'}
# message = input('Введите сообщение: ')
# for z in commas:
#     message = message.replace(z, '')
# lst = message.split()  # все слова
# res = sorted(set(lst) - stop_words)
# for a, b in enumerate(res, 1):
#     print(f'{a}. {b}')
