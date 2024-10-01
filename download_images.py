import csv
import requests
import os

# Ruta del archivo CSV
csv_file_path = 'DataBase.csv'

# Enlace base
base_url = "https://cube.rider.biz/visualcube.php?fmt=png&size=500&stage=oll&view=plan&bg=t"

# Crear un directorio para guardar las imágenes si no existe
output_dir = 'downloaded_images'
os.makedirs(output_dir, exist_ok=True)

# Abrir el archivo CSV y leer los datos
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Omitir la primera fila (encabezado)
    next(reader)
    
    # Iterar sobre las filas del archivo CSV
    for row in reader:
        if len(row) >= 6:  # Verificar que al menos haya 8 columnas
            # Obtener los valores de las columnas necesarias
            columna_4_valor = row[3]  # algoritmo
            columna_3_nombre = row[2]  # Nombre

            # Verificar si la columna 6 contiene "Main Algorithm" o "It's ready"
            if "Main Algorithm" in columna_4_valor:
                columna_4_valor = "D"  # Modificar el algoritmo a "U"
            
            # Generar el enlace con la variación de stage
            enlace = f"{base_url}&case={columna_4_valor}"
            
            # Depuración: imprimir el enlace generado
            print(f"Enlace generado: {enlace}")
            
            # Descargar la imagen
            response = requests.get(enlace)
            
            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                # Definir la ruta del archivo
                archivo_nombre = f"{columna_3_nombre}.png"
                archivo_ruta = os.path.join(output_dir, archivo_nombre)
                
                # Guardar la imagen en el archivo
                with open(archivo_ruta, 'wb') as f:
                    f.write(response.content)
                
                print(f"Imagen descargada y guardada como {archivo_nombre}")
            else:
                print(f"Error al descargar la imagen desde {enlace} (Código de estado: {response.status_code})")
        else:
            print("Fila con menos de 8 columnas encontrada.")

print("Fin del Codigo")
