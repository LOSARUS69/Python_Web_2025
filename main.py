# Строки (immutable, iterable)
# Начало и окончание строки
# 1. replace('что', 'на что') - полная замена
# 2. replace('что', 'на что', сколько раз) - число замен

s = '+7-012-345-67-89' # => +7 (012) 345-67-89

print(s.replace('-',
                ' (',
                1).replace('-', ') ', 1))


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
