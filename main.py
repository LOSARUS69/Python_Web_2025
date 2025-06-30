# Кортеж (tuple, immutable)
# Студент и средний балл

N = 3
students = []

for _ in range(N):
    student, average = input('ФИО: '), float(input('Ср. балл: '))
    students.append((student, average))

print(students)

for st in students:
    student, average = st
    print('Студент: ', student)
    print('Средний балл: ', average)
