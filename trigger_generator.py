import csv
import re

# Función para reemplazar las secuencias especificadas en el texto
def replace_sequences(text):
    sequences = ["R U R' U'",  # Sexy move
                 "R' F R F'",  # Sledge
                 "U R U' R'",  # Anti Sexy move
                 "R U R' U",   # Circle
                 "r U R' U'",  # Fat Sexy move
                 "R U' R' U",
                 "R U' R' U'", # Anti Circle
                 "R' U' R U'", # Reverse Circle
                 "R' U R U'",
                 "U R' U R",   # Push
                 "U' R U' R'", # Another Push
                 "U' R U R'",
                 "U R' U' R",
                 "F R' F' R",  # Hedge
                 "R U R' F'",  # J Trigger
                 "R2 U R' U'",
                 "R2 U R2' U'",
                 "R U2 R' U'",
                 "R U2 R' U2'",
                 "R U2' R' U",
                 "R U2' R' U2",
                 "R U R U'",
                 "R U' R U",
                 "r' F R F'",
                 "F' r U r'", # Lefty insert


                 ############### Tres movimientos

                 "R U2 R'",    # Apertura
                 "R' U2 R",
                 "R U R'",     # Insert
                 "R U' R'",    # Another insert
                 "F' U' F",    # F Insert 
                 "R' U' R",    # Reverse Insert 
                 "R' U R",
                 "f R f'",     # Feliks Insert
                 "f R' f'",
                 "f U f'",
                 "r U r'",     # Fat Push
                 "r U' r'",    # Fat Insert
                 "r' U' R U M'", # CubeHead Insert
                 "l U L' U' M'", # Lefty CubeHead Insert

                 ################ Lefty
                 "L' U' L U",  # Sexy move
                 "L F' L' F",  # Sledge
                 "U' L' U L",  # Anti Sexy move
                 "L' U' L U'",   # Circle
                 "l' U' L U",  # Fat Sexy move
                 "L' U L U'",
                 "L' U L U", # Anti Circle
                 "L U L' U", # Reverse Circle
                 "L U' L' U",
                 "U' L U' L'",   # Push
                 "U L' U L", # Another Push
                 "U L' U' L",
                 "U' L U L'",
                 "F' L F L'",  # Hedge
                 "L' U' L F",  # J Trigger
                 "L2 U' L U",
                 "L2' U' L2 U",
                 "L' U2 L U",
                 "L' U2 L U2'",
                 "L' U2' L U'",
                 "L' U2' L U2",
                 "L' U' L' U",
                 "L' U L' U'",
                 "l F' L' F",


                 ############### Tres movimientos

                 "L' U2 L",    # Apertura
                 "L U2 L'",
                 "L' U' L",     # Insert
                 "L' U L",    # Another insert
                 "F U F'",    # F Insert 
                 "L U L'",    # Reverse Insert 
                 "L U' L'",
                 "f' L' f",     # Feliks Insert
                 "f' L f",
                 "f' U' f",
                 "l' U' l",     # Fat Push
                 "l' U l"    # Fat Insert

                 ]

    for seq in sequences:
        # Crear una expresión regular para detectar la secuencia que no esté entre paréntesis
        # y que esté seguida de un espacio o al final de la línea.
        pattern = rf'(?<!\()({re.escape(seq)})(\s|$)(?!\))'
        # Reemplazar la secuencia en el texto con paréntesis
        text = re.sub(pattern, r'(\1)\2', text)

    return text

# Leer el archivo CSV, procesar las columnas 4, 5, 6 y 7, luego escribir el resultado en un nuevo archivo
def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)  # Convertir el lector en una lista para poder modificarla

    for i, row in enumerate(rows):
        if i == 0:  # Omitir el encabezado
            continue
        # Procesar columnas 4, 5, 6 y 7 (índices 3,4,5, 6)
        row[3] = replace_sequences(row[3])  # Columna 4
        row[4] = replace_sequences(row[4])  # Columna 5
        row[5] = replace_sequences(row[5])  # Columna 6
        row[6] = replace_sequences(row[6])  # Columna 7
        row[6] = replace_sequences(row[8])  # Columna 9

    # Escribir el CSV modificado en un nuevo archivo
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Nombre del archivo CSV de entrada y salida
input_csv = 'DataBase.csv'
output_csv = 'DataBase.csv'

# Llamar a la función para procesar el CSV
process_csv(input_csv, output_csv)

print("Termine :)")