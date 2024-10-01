import subprocess
import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Registrar la fuente Montserrat y Montserrat-Medium
pdfmetrics.registerFont(TTFont('Montserrat', 'Montserrat-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Montserrat-Medium', 'Montserrat-Medium.ttf'))

# Crear un documento PDF
pdf_file = "OLL_cases.pdf"
document = SimpleDocTemplate(
    pdf_file, 
    pagesize=letter,
    rightMargin=85.05,  # Ajustar el margen derecho (en puntos, 1 inch = 72 puntos)
    leftMargin=85.05,   # Ajustar el margen izquierdo
    topMargin=70.875,    # Ajustar el margen superior
    bottomMargin=70.875  # Ajustar el margen inferior
)
width, height = letter  # Obtener las dimensiones de la página

# Definir estilos
styles = getSampleStyleSheet()

title_style = ParagraphStyle(name='Title', fontName='Montserrat-Medium', fontSize=20, alignment=1, spaceAfter=12)
subtitle_style = ParagraphStyle(name='Heading2', fontName='Montserrat-Medium', fontSize=16, alignment=1, spaceAfter=12)
subsub_style = ParagraphStyle(name='Heading3', fontName='Montserrat-Medium', fontSize=14, spaceAfter=12)
subsubsub_style = ParagraphStyle(name='Heading4', fontName='Montserrat-Medium', fontSize=12, spaceAfter=12)
author_style = ParagraphStyle(name='CenteredText', fontName='Montserrat', fontSize=10, alignment=1)
text_style = ParagraphStyle(name='CenteredText', fontName='Montserrat', fontSize=12, leading=16)
text_medium_style = ParagraphStyle(name='CenteredText', fontName='Montserrat-Medium', fontSize=12, leading=12)
text_set_up_style = ParagraphStyle(name='SetUpStyle', fontName ='Montserrat', fontSize=10, alignment=2)  # 0=izquierda, 1=centro, 2=derecha

# Función para crear una tabla de 2x1
def create_2x1_table(image_path, set_up_lines, name_lines, text_lines):

    # Crear el párrafo para la línea de Set Up
    set_up_paragraph = Paragraph('<font name="Montserrat" size="10">{}</font>'.format('<br/>'.join(set_up_lines)), text_set_up_style)
    
    # Crear el párrafo para el nombre
    name_paragraph = Paragraph('<font name="Montserrat-Medium" size="12">{}</font>'.format('<br/>'.join(name_lines)), text_medium_style)
    
    # Crear una lista de párrafos para las líneas de texto
    text_paragraphs = [Paragraph('<font name="Montserrat" size="12">{}</font>'.format(line), text_style) for line in text_lines]
    
    # Combinar los párrafos del nombre, un Spacer, y las líneas de texto
    content = [set_up_paragraph, Spacer(1, -7), name_paragraph, Spacer(1, 6)] + text_paragraphs  # Agregar un Spacer después del nombre
    # El espacio negativo en Spacer(1, -5) es para que set_up_paragraph y name_oaragraph esten aproximadamente a la misma altura

    data = [
        [Image(image_path, width=0.984*inch, height=0.984*inch),
         content]  # Insertar el contenido con Spacer en la tabla
    ]
    
    table = Table(data, colWidths=[1.37*inch, width - 1.37*inch - 2.5422*inch])  # Ajustar el ancho de la tabla
    table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    
    return table

# Leer el archivo CSV y generar tablas
content = []

# Título
title = Paragraph("OLL", title_style)
content.append(title)

# Nombre
author = Paragraph("RedCyclone05", author_style)
content.append(author)

# Saltar un espacio pequeño
content.append(Spacer(1, 12))

# Variables para almacenar el último subtema, subsubtema y subsubsubtema
last_subsubsubtema = ""


# Leer el archivo CSV
csv_file = 'DataBase.csv'
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Omitir la primera fila (encabezados)
    
    for row in reader:
        if row:
            subsubsubtema = row[0] # Grupo
            image_filename = row[1]  # La segunda columna contiene el nombre de la imagen
            name_lines = row[2:3]  # La tercera columna tiene el nombre
            text_lines = row[3:6]  # Las celdas de la 4 a la 6 se consideran líneas de texto
            set_up_lines = row[6:7] # La decima columna tiene el Set Up


            # Construir la ruta completa de la imagen
            image_path = os.path.abspath(os.path.join('downloaded_images', image_filename))
            # Depuración de la ruta de la imagen
            print(f"Buscando la imagen en: {image_path}")


            # Solo agregar un nuevo subsubsubtema si es diferente al último visto
            if subsubsubtema != last_subsubsubtema:
                content.append(Paragraph(subsubsubtema, subsubsub_style))
                last_subsubsubtema = subsubsubtema

            # Crear y agregar la tabla de 2x1 para cada fila del CSV
            table = create_2x1_table(image_path, set_up_lines, name_lines, text_lines)

            content.append(table)

            # Saltar un espacio pequeño
            content.append(Spacer(1, 12))

# Definir un estilo para el párrafo de sugerencia con justificación
suggestion_style = ParagraphStyle(name='SuggestionText', fontName='Montserrat', fontSize=12, leading=16, alignment=4)

# Crear el párrafo con el nuevo estilo de justificación
suggestion_paragraph = Paragraph(
    """
    <font name="Montserrat" size="12">
    My suggestion is to learn the first algorithm for each case. If you don't like it, use the second one, and if you don’t like the second one, use the third. I recommend that you learn one per day following the order presented in this PDF. Learn it with the triggers, which are those small movements in parentheses, and practice it many times until you master it.
    </font>
    """, 
    suggestion_style
)

# Agregar el párrafo con el texto justificado
content.append(suggestion_paragraph)


# Agregar sección de Referencias
content.append(Paragraph("Referencias", subtitle_style))

# Lista de referencias con solo el link cliqueable, en azul y subrayado
referencias = [
    'VisualCube: Generate custom Rubik\'s cube visualisations from your browser address bar: <a href="https://cube.rider.biz/visualcube.php" color="blue"><u>https://cube.rider.biz/visualcube.php</u></a>',
    'VisualCube: Cube image in each algorithm: <a href="https://cube.rider.biz/visualcube.php?fmt=png&size=500&stage=oll&view=plan&bg=t&case=D" color="blue"><u>https://cube.rider.biz/visualcube.php?fmt=png&size=500&stage=oll&view=plan&bg=t&case=D</u></a>',
    'SpeedCubeDB: OLL Algorithms: <a href="https://speedcubedb.com/a/3x3/OLL" color="blue"><u>https://speedcubedb.com/a/3x3/OLL</u></a>',
    'CubeSkills: OLL Cases: <a href="https://www.cubeskills.com/tutorials/oll-algorithms" color="blue"><u>https://www.cubeskills.com/tutorials/oll-algorithms</u></a>',
    'CubeHead: How to Learn Full OLL in ONE MONTH (easy)  <a href="https://www.youtube.com/watch?v=Ysy1S8ADzqw&t=230s" color="blue"><u>https://www.youtube.com/watch?v=Ysy1S8ADzqw&t=230s</u></a>',
    'CubeHead: Full OLL: Algorithms & Finger Tricks [My Algs 2024]  <a href="https://www.youtube.com/watch?v=Q947zZRYMdg&t=10s" color="blue"><u>https://www.youtube.com/watch?v=Q947zZRYMdg&t=10s</u></a>',
    'GitHub: Repository with which the images and this document were created: <a href="https://github.com/RedCyclone05/OLL" color="blue"><u>https://github.com/RedCyclone05/OLL</u></a>'
]

# Agregar cada referencia como un bullet con enlace cliqueable
for referencia in referencias:
    bullet = Paragraph(f"• {referencia}", text_style)
    content.append(bullet)

# Saltar un espacio pequeño
content.append(Spacer(1, 12))

# Construir el PDF
document.build(content)

# Abrir el PDF
if subprocess.run(['start', pdf_file], shell=True).returncode != 0:
    print(f"No se pudo abrir el PDF '{pdf_file}'.")
else:
    print(f"PDF '{pdf_file}' creado y abierto con éxito.")

print("Fin del Codigo")