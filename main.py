# Меняем значения переменных местами
a = 3
b = 5

print('До:')
print('a =', a, 'b =', b)

a, b = b, a  # swap

print('После:')
print('a =', a, 'b =', b)
