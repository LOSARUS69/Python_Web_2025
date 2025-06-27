# Строки (immutable, iterable)
# Задача: исправить букву в слове сабака
s = 'сабака'
res = ''

for i in range(len(s)):
    if i == 1: # я знаю, что по индексу 1 надо написать 'o'
        res += 'о'
    else:
        res += s[i]

print(res)
