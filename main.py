# Формат вывода
# \ - начало escape sequence ("экран")
# \n - перевод строки
# \t - табуляция
# \x - вывод символа по 2-знакоместам 16-формате (ASCII)
# \u - вывод символа по 4-знакоместам 16-формате (Unicode)
# Burned Again Shell - BUSH
word1 = 'пришел'
word2 = 'увидел'
word3 = 'победил'
word4 = '27\xB0C'  # ASCII

print(word1, word2, word3, end=' -> ', sep=', ')
print(word4)
print('Концерт группы \"Кино\"')
print('Путь к файлу: С:\\Program Files\\bin')
