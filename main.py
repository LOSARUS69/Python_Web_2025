# match - case (работает с версии 3.10 >)
flag = True
print('Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо,\n\tQ - выход')

while flag:
    ch = input('Ваш выбор: ')
    match ch:
        case 'L' | 'l' | 'д' | 'Д':
            print('Свернули налево')
        case 'R' | 'к' | 'r' | 'К':
            print('Свернули направо')
        case 'F' | 'а' | 'А' | 'f':
            print('Пошли прямо')
        case 'Q' | 'q' | 'й' | 'Й':
            print('До свидания!')
            flag = False
        case _:  # default
            print('Выбор не ясен')
