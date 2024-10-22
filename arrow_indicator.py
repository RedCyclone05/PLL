import webbrowser
import tkinter as tk
import csv
import time

# Variables globales
pares_registrados = []  # Lista para almacenar los pares registrados
ultimo_clic = None

# Booleano para hacer el delay
primer_uso = True

# Función para manejar los clics en los botones
def registrar_clic(boton_id):
    global ultimo_clic
    if ultimo_clic is None:
        # Si es el primer clic, almacenarlo
        ultimo_clic = boton_id
    else:
        # Crear un par con el clic anterior y el actual, y registrarlo, Se coloca U antes de cada numero y -s8 al final de cada par
        pares_registrados.append(f"U{ultimo_clic}U{boton_id}-s8")
        print(f"Par registrado: U{ultimo_clic}U{boton_id}-s8")
        ultimo_clic = None  # Reiniciar para el siguiente par

# Función para abrir el navegador y la interfaz
def abrir_interfaz(case_url, row_index, csv_data, csv_file):
    # Abrir el link en el navegador
    webbrowser.open(case_url)

    global primer_uso # Se llama a la variable global

    if primer_uso == True:
        # Añadir un pequeño retraso para que el navegador tenga tiempo de cargar
        time.sleep(1)
        primer_uso = False # Cambiar el booleano para que solo haga delay la primera vez que se ejecuta

    # Crear la interfaz gráfica con tkinter
    root = tk.Tk()
    root.title(f"Interfaz 3x3 - Fila {row_index + 1}")

    # Ajustar el tamaño de la ventana
    root.geometry("300x300")

    # Mantener la ventana de tkinter siempre al frente
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)  # Asegurar que esté al frente solo al abrir

    # Crear una cuadrícula 3x3 de botones numerados
    for i in range(3):
        for j in range(3):
            boton_id = i * 3 + j  # Número de 0 a 8
            boton = tk.Button(root, text=str(boton_id), font=("Arial", 24), width=5, height=2, 
                              command=lambda boton_id=boton_id: registrar_clic(boton_id))
            boton.grid(row=i, column=j)

    # Ejecutar la ventana hasta que se cierre
    root.mainloop()

    # Verificar si la fila tiene al menos 8 columnas; si no, agregar columnas vacías
    while len(csv_data[row_index]) < 8:
        csv_data[row_index].append("")

    # Guardar los pares registrados en la columna 8 (índice 7)
    csv_data[row_index][7] = ','.join(pares_registrados)  # Guardar los pares en formato CSV

    # Limpiar pares para el siguiente registro
    pares_registrados.clear()

    # Guardar los cambios en el archivo CSV
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

# Función principal para leer el CSV y procesar cada fila
def procesar_csv(csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        csv_data = list(reader)

    # Iterar sobre las filas del CSV, omitiendo la cabecera
    for row_index, row in enumerate(csv_data[1:], start=1):
        case_value = row[3]  # Columna 4 contiene el "case"
        case_url = f"https://cube.rider.biz/visualcube.php?fmt=png&size=500&stage=pll&view=plan&bg=t&case={case_value}"

        # Verificar si la columna 6 contiene "Main Algorithm" o "It's ready"
        if "Main Algorithm" in case_url:
            case_url = "https://cube.rider.biz/visualcube.php?fmt=png&size=500&stage=pll&view=plan&bg=t&case=D"  # Modificar el algoritmo a "D"

        # Abrir la interfaz y registrar los pares
        abrir_interfaz(case_url, row_index, csv_data, csv_file)

# Nombre del archivo CSV
csv_file = 'DataBase.csv'

# Ejecutar el procesamiento del CSV
procesar_csv(csv_file)

