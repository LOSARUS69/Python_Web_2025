# Кортеж (tuple, immutable)
# Функция sorted() - возвращает сортированный список

s = {'Крутов', 'Селезнёв', 'Митрофанова'}
r = False

lst = sorted(s, reverse=r)

# lst = list(s)
# lst.sort()

print(*lst, sep=', ')
