import csv
import os
import genanki

# Solicitar nombre del deck y archivo CSV al usuario
deck_name = input("\nIntroduce el nombre del deck: ")

csv_name = 'DataBase.csv'
output_apkg = f'{deck_name}.apkg'
image_folder = 'downloaded_images'

# Reemplazar espacios en el nombre del deck con guiones bajos
deck_name_sanitized = deck_name.replace(' ', '_')

# Crear un modelo para las tarjetas con 6 campos
model_id = 1607392315
model = genanki.Model(
  model_id,
  'Simple ModelOLL',
  fields=[
    {'name': 'Front'},      # Campo 1
    {'name': 'Back'},       # Campo 2 (imagen)
    {'name': 'Field1'},     # Campo 3 (columna 6 del CSV)
    {'name': 'Field2'},     # Campo 4 (columna 7 del CSV)
    {'name': 'Field3'},     # Campo 5 (columna 8 del CSV)
    {'name': 'Field4'},     # Campo 6 (columna 9 del CSV)
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '''
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
          <div style="text-align:center; font-size: 24px;">
            Set Up:
            <div style="font-size: 20px;">
              {{Front}}
            </div>
          </div>
        </div>
      ''',
      'afmt': '''
        <div style="text-align:center;">
          <div style="display:inline-block;">
            <div style="margin-bottom: 10px;">
              <img src="{{Back}}" style="width: 25vw;">
            </div>
            <div style="text-align: center; font-size: 20px;">
              <div style="margin-bottom: 5px;">{{Field1}}</div>
              <div style="margin-bottom: 5px;">{{Field2}}</div>
              <div style="margin-bottom: 5px;">{{Field3}}</div>
              <div>{{Field4}}</div>  <!-- Columna 9 debajo de las anteriores -->
            </div>
          </div>
        </div>
      ''',
    },
  ])

# Crear un deck
deck_id = 2059400211
deck = genanki.Deck(
  deck_id,
  deck_name_sanitized)

# Leer el archivo CSV y generar las tarjetas
with open(csv_name, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # Saltarse el primer renglón (encabezados)
    next(reader)
    
    rows = list(reader)
    
    for row in rows:
        # Columna 7 (anverso)
        front = row[6]
        
        # Columna 2 es el nombre de la imagen en processed_downloaded_images
        image_name = row[1]
        image_path = os.path.join(image_folder, image_name)
        
        # Verificar si la imagen existe
        if os.path.exists(image_path):
            image_tag = f'{image_name}'
        else:
            image_tag = '[Imagen no encontrada]'
        
        # Columnas 4, 5, 6  (contenido adicional en el reverso)
        field1 = row[3]  # Columna 4
        field2 = row[4]  # Columna 5
        field3 = row[5]  # Columna 6
        field4 = row[6]  # Vacio
        
        # Crear una nueva nota (tarjeta) con los 6 campos
        note = genanki.Note(
            model=model,
            fields=[front, image_tag, field1, field2, field3, field4]
        )
        
        # Añadir la nota al deck
        deck.add_note(note)

# Crear el paquete y añadir las imágenes
package = genanki.Package(deck)

# Añadir las imágenes al paquete
package.media_files = [os.path.join(image_folder, row[1]) for row in rows if os.path.exists(os.path.join(image_folder, row[1]))]

# Guardar el archivo .apkg
package.write_to_file(output_apkg)

print(f"Baraja de Anki generada correctamente: {output_apkg}")
