# Пишем и подключаем свои модули
# from . lib import summ - из текущей директории
# from .. lib import summ - уровнем выше
# from .lib import summ - относительный импорт
from lib import summ


def main():
    print(summ(7, 3))


if __name__ == '__main__':
    main()

# Работа с формулами:
# ....
# ws['A1'] = "=SUM(A1:A10)"
# Формат:
# from openpyxl import load_workbook
# from openpyxl.styles import Font, Alignment
# # ....
# wb = load_workbook('docs/employees.xlsx')
# ws = wb.active
# ws['A1'].font = Font(bold=True, size=14)
# ws['A1'].alignment = Alignment(horizontal="center")

# Чтение данных
# from openpyxl import load_workbook
#
# wb = load_workbook('docs/employees.xlsx')
# ws = wb.active
#
# rows_count = ws.max_row # число заполненных строк
#
# for row in ws.iter_rows(min_row=2, values_only=True):
#     fio, pos, dept = row
#     print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dept}')

# from openpyxl import load_workbook
#
# # Открываем (загружаем) рабочую книгу
# wb = load_workbook('docs/report.xlsx')
#
# # Активный лист
# ws = wb.active
# # Можно и по имени
# # ws = wb['Отчёт']
#
# # Заголовки
# ws['A1'] = 'ФИО'
# ws['B1'] = 'Должность'
# ws['C1'] = 'Отдел'
#
# # Данные
# employees = [
#     ['Иванов И.И.', 'Менеджер', 'Продажи'],
#     ['Петров П.П.', 'Бухгалтер', 'Финансы'],
#     ['Сидорова С.С.', 'Аналитик', 'IT'],
# ]
#
# for row, data in enumerate(employees, start=2):
#     ws.cell(row=row, column=1, value=data[0])
#     ws.cell(row=row, column=2, value=data[1])
#     ws.cell(row=row, column=3, value=data[2])
#
# wb.save('docs/employees.xlsx')

# Способы записи
# ws['F1'] = 'Привет мир'
# ws.cell(row=1, column=3, value='Hello')

# wb.save('docs/newtable.xlsx')

# # Пустой Excel-файл
# from openpyxl import Workbook
#
# wb = Workbook() # wb - Workbook
#
# ws = wb.active
# ws.title = 'Отчёт'
#
# wb.save('docs/report.xlsx')

# from docxtpl import DocxTemplate
#
# # Загрузка шаблона
# doc = DocxTemplate('docs/template.docx')
#
# # Данные для подстановки в шаблон
# content = [
#     {
#         'company': 'OOO "Монолит"',
#         'employee': 'Петров Д.И.',
#         'position': 'Менеджер',
#         'date': '01/01/2025'
#     },
#     {
#         'company': 'OOO "Арсенал"',
#         'employee': 'Иванов Д.И.',
#         'position': 'Инженер',
#         'date': '01/01/2025'
#     }
# ]
#
# count = 1
# for item in content:
#     doc.render(item)
#     doc.save(f'docs/about{count}.docx')
#     count += 1

# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.shared import Cm, Inches, Mm, Pt # Для размеров
#
# doc = Document()  # создание экземпляра документа
#
# # Добавление заголовка
# doc.add_heading('Отчёт за месяц', 1)
# paragraph = doc.add_paragraph()
# paragraph = doc.add_paragraph('В этом отчёте представлены')
# # run - что-то внутри абзаца
# paragraph.add_run(' ключевые показатели').bold = True
# # Новый абзац для списка
# paragraph = doc.add_paragraph()
# paragraph_format = paragraph.paragraph_format
# paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
# # Маркированный
# paragraph = doc.add_paragraph('Первый пункт', style='List Bullet')
# paragraph = doc.add_paragraph('Второй пункт', style='List Bullet')
#
# # Нумерованный
# paragraph = doc.add_paragraph('Первый пункт', style='List Number')
# paragraph = doc.add_paragraph('Второй пункт', style='List Number')
#
# paragraph = doc.add_paragraph()
# # Добавляем таблицу
# table = doc.add_table(rows=3, cols=3)
#
# # Заполняем
# for i, row in enumerate(table.rows):
#     for j, cell in enumerate(table.cells):
#         cell.text = f'Строка {i + 1}, Столбец {j + 1}'
#
# doc.add_paragraph()
# doc.add_picture('images/sunny_day.jpg', width=Mm(105))
#
# doc.save('docs/report.docx')

# from PIL import Image, ImageFilter, ImageEnhance
#
# orig = Image.open('images/python.jpg').convert('RGB')
# Размытие
# blur_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# blur_image.show()

# # Усиление резкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image = enchancer.enhance(4.0)
# sharpened_image.show()

# Получить контуры
# edges = orig.filter(ImageFilter.FIND_EDGES)
# edges.show()


# from PIL import Image
#
# orig = Image.open('images/sunny_day.jpg').convert('RGB')
#
# up = orig.crop((0, 0, 600, 200))
# down = orig.crop((0, 200, 600, 400))
#
# new = Image.new('RGB', (600, 400))
#
# new.paste(down, (0, 0))
# new.paste(up, (0, 200))
#
# new.show()
#
#

# from PIL import Image, ImageDraw, ImageFont
#
# # https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
# W = 600
# H = 400
#
# image = Image.new('RGB',
#                   (W, H),
#                   (0, 163, 232))
#
# draw = ImageDraw.Draw(image)
#
# text = 'Солнечный день'
# # draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
# draw.circle((600, 0), 100, fill='yellow')
# font = ImageFont.truetype(
#     # font='arial.ttf',  # можно использовать любой установленный шрифт
#     font='fonts/Geisha.ttf',
#     size=50
# )
# # Получаем размеры текста
# _, _, w, h = draw.textbbox((0, 0), text, font=font)
#
# # Рассчитываем позицию для центрирования
# x = (W - w) // 2
# y = (H - h) // 2
#
# draw.text((x, y), text, fill=(255, 255, 0), font=font)
#
# # image.save('images/sunny_day.jpg')
# image.show()
