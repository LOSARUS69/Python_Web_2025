# Внешние библиотеки
# Документы по шаблону (template.docx)
# Word - DOCX (docxtpl)
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
from docxtpl import DocxTemplate

# Загрузка шаблона
doc = DocxTemplate('docs/template.docx')

# Данные для подстановки в шаблон
content = [
    {
        'company': 'OOO "Монолит"',
        'employee': 'Петров Д.И.',
        'position': 'Менеджер',
        'date': '01/01/2025'
    },
    {
        'company': 'OOO "Арсенал"',
        'employee': 'Иванов Д.И.',
        'position': 'Инженер',
        'date': '01/01/2025'
    }
]

count = 1
for item in content:
    doc.render(item)
    doc.save(f'docs/about{count}.docx')
    count += 1

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
