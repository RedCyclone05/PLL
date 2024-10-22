import pandas as pd

# Leer el archivo CSV sin encabezados
df = pd.read_csv('DataBase.csv', header=None)

# Función para procesar el texto de la columna 6
def process_text(text):
    if text == "Main Algorithm":
        return "Set Up Algorithm"
    
    # Voltear el texto en orden inverso
    reversed_text = text[::-1]
    
    # Separar los elementos por espacio
    elements = reversed_text.split()
    
    # Procesar cada elemento
    processed_elements = []
    for element in elements:
        if "'" in element:
            # Eliminar apóstrofo si está presente
            processed_elements.append(element.replace("'", ""))
        else:
            # Agregar apóstrofo si no está presente
            processed_elements.append(element + "'")
    
    # Unir los elementos procesados con espacio
    processed_text = ' '.join(processed_elements)
    
    # Reemplazar las secuencias "2?'" y "2?" por "?2"
    processed_text = processed_text.replace("2U'", "U2").replace("2U", "U2")
    processed_text = processed_text.replace("2D'", "D2").replace("2D", "D2")
    processed_text = processed_text.replace("2R'", "R2").replace("2R", "R2")
    processed_text = processed_text.replace("2L'", "L2").replace("2L", "L2")
    processed_text = processed_text.replace("2F'", "F2").replace("2F", "F2")
    processed_text = processed_text.replace("2B'", "B2").replace("2B", "B2")
    processed_text = processed_text.replace("2M'", "M2").replace("2M", "M2")
    processed_text = processed_text.replace("2S'", "S2").replace("2S", "S2")
    processed_text = processed_text.replace("2E'", "E2").replace("2E", "E2")
    processed_text = processed_text.replace("2y'", "y2").replace("2y", "y2")
    processed_text = processed_text.replace("2x'", "x2").replace("2x", "x2")
    processed_text = processed_text.replace("2z'", "z2").replace("2z", "z2")
    processed_text = processed_text.replace("2u'", "u2").replace("2u", "u2")
    processed_text = processed_text.replace("2d'", "d2").replace("2d", "d2")
    processed_text = processed_text.replace("2r'", "r2").replace("2r", "r2")
    processed_text = processed_text.replace("2l'", "l2").replace("2l", "l2")
    processed_text = processed_text.replace("2f'", "f2").replace("2f", "f2")
    processed_text = processed_text.replace("2b'", "b2").replace("2b", "b2")

    return processed_text

# Procesar cada fila en la columna 4 (índice 3) y escribir en la columna 9 (índice 8)
if len(df.columns) > 3:
    df[8] = df[3].apply(process_text)

    # Asignar "Set Up" al primer elemento de la columna 10
    if not df.empty:
        df.at[0, 8] = "Set Up"

    # Guardar el DataFrame modificado en el archivo CSV
    df.to_csv('DataBase.csv', index=False, header=False)

    print("Proceso completado. El archivo CSV ha sido actualizado.")
else:
    print("El archivo CSV no tiene suficientes columnas.")
