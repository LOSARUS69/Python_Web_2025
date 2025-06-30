# Кортеж (tuple, immutable)
BLACK = (0, 0, 0)
empty = ()  # tuple()
one = (1,)
temper = 36, 6
s = 'Python'
t = tuple(s) + ('.',)
print(t)

cards = [(7, 'червей'), ('туз', 'пик')]

print((1, 2) < (1, 3))
a = 3
b = 4

a, b = b, a