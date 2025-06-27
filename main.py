# Строки (immutable, iterable)
# Задача: посчитать гласные в слове
s = 'язык python'

v = 0 # Число гласных

for ch in s:
    # if ch in {'а', 'е', 'и', 'о', 'у',
    #           'ы', 'э', 'ю', 'я', 'y', 'o'}:
    if ch in 'аеёиоуыэюяyo':
        v += 1

print(f'Число гласных в строке "{s}" = {v}')

# Перебор строки по числовому индексу
for index in range(len(s)):
    print(s[index])