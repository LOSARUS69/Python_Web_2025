# Iterable object
# len() - сколько элементов объекте
# a = 123456  # int - не является iterable
#
# length = len(str(a))  # поэтому конвертируем в str
# print(length)

word = input('Введите слово для анализа длины: ')
if not word or len(word) < 4:
    print('Вы ничего не ввели или слово слишком короткое')
else:
    print('Длина слова "' + word + '" =', len(word))
