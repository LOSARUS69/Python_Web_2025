# break, continue
num = 3  # число, которое надо угадать
var = ''

print('Я загадал число, угадай!')

while True:
    var = int(input('Ваше значение: '))
    if var == num:
        print('Ура. Угадал!')
        break
    elif var > num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')

print('Приходи ещё!')
