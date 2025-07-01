# ДЗ
# Фраза: ну я типо вообще короче не понимаю этот язык
stop_words = {'ну', 'типо', 'короче', 'не'}
message = input('Введите сообщение: ')
lst = message.split() # все слова
res = sorted(set(lst) - stop_words)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')