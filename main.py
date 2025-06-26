# match - case (3.10 >)
height = int(input('Введите рост: '))

while not (150 <= height <= 180):
    print(f'Рост кандидата {height} не подходит')
    height = int(input('Введите рост: '))

print('Кандидат выбран')