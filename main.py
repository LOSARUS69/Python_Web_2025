# Строки (immutable, iterable)
# две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код) - возвращает символа по Unicode-коду

# abc = 'абвгдеёжзийклмнопрстуфхцшщъыьэюя'
phrase = 'Язык Python'

print(phrase.lower())  # все маленькие
print(phrase.upper())  # все большие
print(phrase.capitalize())  # только 1-я буква заглавная
print(phrase.title())  # все слова с заглавной
print('Ура! ' * 3)  # Повторение строки
print('Телевизор'.count('е'))  # Количество вхождений подстроки
print('Python'.index('h'))  # Индекс символа

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
