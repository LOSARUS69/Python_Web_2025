# Cписки (list)

# lst = []  # пустой список
lst = [1, 7, 3, 5, 6, 4]
lst.append(2)
lst.sort()
lst.reverse()

print(lst)

a = ['a', 'b', 'c']
b = a[:]  # a.copy()
b.append('d')  # b += ['d']
print(id(a))
print(id(b))
print(a)
print(b)

['append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
