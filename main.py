# PEP8 - правила именования
# c, l, O, I
# Операции над множествами
a = {3, 5, 7}
b = {3, 5, 7, 9, 11}

# Объединение множеств
c = a.union(b)
# c = a | b
print(c)

# Пересечение
c = a.intersection(b)  # и там, и там
# c = a & b
print(c)

# Разность
c = b.difference(a)  # есть в 1-м, но нет во 2-м
# c = b - a
print(c)

# Симметричная разность
c = a.symmetric_difference(b)  # есть только в одном из двух
# c = b ^ a
print(c)
