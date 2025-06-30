# Строки (immutable, iterable)
# Cрез (у строки и у других коллекций, кроме set)
# [начало:окончание:шаг]

s = 'Дорог Рим'  # + и *
# Город Миргород

temp = s.lower()
city = temp[:5][::-1]
res =  city + ' ' + temp[6:][::-1] + city

print(res.title())



