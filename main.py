# Кортеж (tuple, immutable)
# Функция enumerate() - в цикле for возвращает пару (i, v)

fio = ['Крутов', 'Митрофанова', 'Селезнёв']

for i, v in enumerate(fio):
    print(f'{i + 1}. {v}.')

