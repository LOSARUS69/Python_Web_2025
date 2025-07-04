# Внешние библиотеки
# Графика
# PIL - Python Imagine Library
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
from PIL import Image, ImageDraw

RED = (255, 0, 0)
POLY = [(50, 50), (150, 50), (180, 120)]

image = Image.new('RGB',
                  (600, 400),
                  (0, 0, 255))

draw = ImageDraw.Draw(image)

draw.line((0, 0, 600, 400),
          fill=RED, width=5)
draw.line((600, 0, 0, 400),
          fill=RED, width=5)
draw.rectangle((10, 10, 590, 390),
               outline=RED, width=10)

draw.ellipse((10, 10, 590, 390),
               outline=RED, width=10)
draw.polygon(POLY, outline='green', width=15)
draw.text((100, 100), 'Текст', fill=RED)

image.save('images/blue.jpg')

# image = Image.open('images/python.jpg')
#
# x, y = image.size
# mode = image.mode
# pixels = image.load()  # загрузить таблицу пикселей
#
# print(f'Ширина = {x}, высота = {y}')
# print(f'Цветовая схема: {mode}')

# image_rotate = image.rotate(90)
# image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# cropped = image.crop((250, 0, 550, 300))
# resized = image.resize((400, 300))

# # Grayscale
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         average = (r + g + b) // 3
#         pixels[i, j] = average, average, average

# # Негатив
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = 255 - r, 255 - g, 255 - b

# # Инверсия
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = g, b, r

# resized.save('images/python2.jpg')

# from pprint import pprint
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# pprint(matrix)

# import datetime as dt
#
# my_time = dt.time(15, 27, 32)
# print(my_time)
# my_day = dt.date(2025, 7, 4)
# print(my_day)
# my_day_time = dt.datetime.combine(my_day, my_time)
# print(my_day_time)
#
# date1 = dt.date(2025, 6, 15)
# date2 = dt.date(2025, 7, 3)
# delta = date2 - date1
#
# print(delta)
#
# print(dt.datetime.now())
# print(dt.datetime.now().date())
# print(dt.datetime.now().time())

# time = dt.datetime.now()
# ftime = time.strftime('%d-%m-%Y')
# print('Сегодня:', ftime)
# ftime = time.strftime('%H:%M:%S')
# print('Время:', ftime)

# import random as r
# r.seed()
# print(r.random())

# N = 8
#
# abc = 'qwertyuiopasdfghjklzxcvbnm'
# num = '1234567890'
# spec = '@#$&'
#
# abc = list(abc)
# num = list(num)
# spec = list(spec)
#
# r.shuffle(abc)
#
# temp = abc[:N - 3]
# temp.append(r.choice(abc).upper())
# temp.append(r.choice(num))
# temp.append(r.choice(spec))
# r.shuffle(temp)
# res = ''.join(temp)
#
# print(res)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for _ in range(10):
#     print(r.sample(lst, k=5))

# zara = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
#
# for _ in range(10):
#     print(r.choice(zara), r.choice(zara))

# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
#
# keys = list(d.keys())
#
# key = r.choice(keys)
# print(d[key])

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = r.choice(lst)
# print(res)

# print(r.choice(['орёл', 'решка']))
# print(r.choice('орёл'))

# for _ in range(10):
#     # print(r.randint(0, 10))
#     print(r.randrange(0, 10, 2))

# import math as m
# from math import *
# from math import pi, sqrt, sin, radians, hypot

# from math import sqrt

# print(dir(m))
# print(help(m.cos))

# print('Число Пи:', pi)
# print('Квадратный корень 4:', sqrt(4))
# print('Синус 30°:', round(sin(radians(30)), 2))
# print('Гипотенуза для 3 и 2: ', hypot(3, 2))


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
