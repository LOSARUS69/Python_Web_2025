# Cписки (list)

lst = []  # пустой список
while (item := input('Ингредиент: ')) != '':
    lst.append(item)

temp = set(lst)
lst = list(temp)

print(f'У нас есть {len(lst)} ингредиентов: ')
lst.sort()

for i in range(len(lst)):
    print(f'\t{i + 1}. {lst[i]}')

['append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
