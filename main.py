# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
# import math as m
# from math import *
from math import pi, sqrt, sin, radians
# from math import sqrt

# print(dir(m))
# print(help(m.cos))

print('Число Пи:', pi)
print('Квадратный корень 4:', sqrt(4))
print('Синус 30°:', round(sin(radians(30)), 2))

# lst = [1, 1, 2, 3, 5]
# # res = 0
# # for x in lst:
# #     res += x
# res = sum(lst)
# min_value = min(lst)
# max_value = max(lst)
# print(res, min_value, max_value)
# import sys
#
# strings = [d.strip('\n') for d in sys.stdin.readlines()]
# length = len(strings)  # сколько строк
# rem = length % 3
#
# if rem:
#     strings = strings[:length - rem]
#
# for x in range(0, length - rem, 3):
#     summ = sum(len(a) for a in strings[x:x + 3])
#     result = []
#     for s in strings[x:x + 3]:
#         temp = s.lower().split()
#         result += filter(lambda a: len(a) % 2 == summ % 2, temp)
#     result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]
#     print(*result, sep='. ')
