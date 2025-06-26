# вывод чисел, закаивающихся на 3 в диапазоне от 1 до 100
counter = 1

while counter <= 100:
    if counter % 10 == 3:
        print(counter, end=', ')
    counter += 1
