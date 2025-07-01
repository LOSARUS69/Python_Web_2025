# Списочные выражения (list comprehension)
# Занести в список каждое третье слово из предложения
text = 'Списочные выражения применяются для эффективности кода'

# res = [a for a in text.split() if (text.index(a) + 1) % 3 == 0]
res = [a for a in text.split()[2::3]]
# операции со списком
print(res)








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
