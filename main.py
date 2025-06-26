# break, continue
counter = 0  # обнуляем счётчик
# цикл из 5 итераций, но 3 пропускаем
while counter < 5:
    counter += 1  # инкремент (краткая запись)
    if counter == 3:
        continue  # прервать текущую итерацию и начать следующую
    print(f'Итерация номер: {counter}')
