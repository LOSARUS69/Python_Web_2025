# Строки (immutable, iterable)
# Шифр Цезаря

# Создаем алфавит
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphabet_u = alphabet.upper()

# Получаем входные данные
message = input('Введите строку: ').strip().lower()
key = int(input('Введите ключ: '))

# Инициализируем пустую строку для результата
encrypted = ''

# Перебираем каждый символ в сообщении
for letter in message:
    # Проверяем, является ли символ буквой из алфавита
    if letter in alphabet:
        # Находим позицию буквы в алфавите
        t = alphabet.index(letter)
        # Вычисляем новую позицию с учетом сдвига
        new_key = (t + key) % len(alphabet)
        # Добавляем зашифрованный символ
        encrypted += alphabet[new_key]
    else:
        # Если символ не буква, оставляем его без изменений
        encrypted += letter

# Для расшифровки достаточно изменить формулу вычисления позиции:
# new_key = (t - key) % len(alphabet)

print('Зашифрованное сообщение:', encrypted)

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
