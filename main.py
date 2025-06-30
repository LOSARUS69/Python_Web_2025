# Cписки (list)
# Создание аббревиатур

lst = []

while (word := input('Введите слово: ').strip()) != '':
    lst.append(word[0].upper())

print('Получилась аббревиатура', end=': ')
print(*lst[:10], sep='')

['append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
