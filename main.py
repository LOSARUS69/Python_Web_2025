# Строки (immutable, iterable)
# Каждая буква повторяется столько раз,
# какое её номер в строке (считаем с 1)

word = 'статор'

for i in range(1, len(word) + 1):
    print(word[i - 1] * i, end='')

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
