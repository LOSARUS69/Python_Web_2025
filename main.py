# Строки (immutable, iterable)
# Начало и окончание строки
# 1. find('подстрока') - с самого начала (0-й индекс)
# 2. find('подстрока', start) - с какого места искать
# 3. find('подстрока', start, end) - с какого по какое

s = 'синхрофазотрон'  # ищем 'о': сколько их и где находятся
ch = 'о'

if ch in s:
    count = s.count(ch)
    print(f'Буква \'{ch}\' встречается в слове "{s}" {count} раз(а).')
    print('Её позиция/позиции:', end=' ')
    start = 0
    for i in range(count):
        pos = s.find(ch, start)
        start = pos + 1
        print(pos, end=' ')
else:
    print(f'Буквы \'{ch}\' нет в слове "{s}".')


"""
['capitalize', 'casefold', 'center', 
 'count', 'encode', 'endswith', 'expandtabs', 
 'find', 'format', 'format_map', 'index', 
 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
 'isprintable', 'isspace', 'istitle', 'isupper', 
 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'removeprefix', 'removesuffix', 
 'replace', 'rfind', 'rindex', 'rjust', 
 'rpartition', 'rsplit', 'rstrip', 'split', 
 'splitlines', 'startswith', 'strip', 
 'swapcase', 'title', 'translate', 'upper', 'zfill']
 """
