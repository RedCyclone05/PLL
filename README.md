# Proyecto PLL

## Descripción

Este proyecto está diseñado para procesar imágenes relacionadas con el paso PLL (Permutation of the Last Layer) del método CFOP del cubo de Rubik. El objetivo es generar un documento PDF que contenga imágenes y detalles relevantes de cada algoritmo de PLL, así como un Deck de Flashcards para Anki, que facilitará el estudio de cada grupo de algoritmos.

1. **Selección de Piezas:**: Abre una imagen del caso PLL y una matriz del caso en la que puedes hacer clic para seleccionar qué piezas se intercambian. Almacena esta información para generar las flechas que se visualizarán en la imagen descargada.
2. **Descarga de Imágenes**: Descarga imágenes desde enlaces generados a partir de un archivo CSV, llamado `DataBase.csv`.
3. **Generar el algoritmo Set Up**: Añade una nueva columna al archivo CSV llamado `DataBase.csv` la cual contiene el algoritmo Set Up, cuya función es plantear el caso a resolver.
4. **Generar los Triggers**: Modifica el archivo CSV llamado `DataBase.csv`, para ello analiza todas las columnas en la cual haya presente un algoritmo y lo divide en pequeños grupos de movimientos llamados Triggers. 
5. **Generación de PDF**: Crea un documento PDF que incluye las imágenes procesadas, los algoritmos provenientes de un archivo CSV llamado `DataBase.csv`, con un formato estético y organizado.
6. **Genera Decks de Anki**: Genera un Deck de Anki por cada grupo seleccionado, le pregunta al usuario, el nombre del Deck.

## Estructura del Proyecto

El proyecto consta de seis scripts principales:

1. **Selección de Piezas:** (`arrow_indicator.py`):Este script abre la imagen de cada caso presente en el archivo CSV y visualiza una matriz de 3x3 que representa una pieza del cubo. El objetivo es seleccionar qué pieza se mueve a qué lugar. Para hacerlo, debes hacer clic en el origen de la pieza (primera selección) y luego en la ubicación de destino (segunda selección). Esto representa el movimiento con una flecha, donde el primer clic indica la "cola" y el segundo la "punta" de la flecha. El script guarda estos movimientos como pares de datos en una nueva columna del CSV. Una vez que completes la selección de una pieza, simplemente cierra la ventana para avanzar al siguiente caso.
En situaciones donde dos piezas se intercambian entre sí, deberás realizar dos selecciones: una para mover la pieza A a la posición de B y otra para mover la pieza B a la posición de A, creando visualmente una flecha de doble punta. La imagen del caso solo sirve de apoyo para saber que piezas se intercambiaran.

2. **Descargar Imágenes** (`download_images.py`): Este script descarga imágenes desde enlaces especificados en un archivo CSV y las guarda en una carpeta local.

3. **Generar el algoritmo SetUp para cada caso** (`set_up_generator.py`): Lee un archivo CSV con informacion sobre cada caso, luego genera un nuevo algoritmo el cual sirve para plantear el caso especifico y luego se le añade a la columna 10 del CSV original.

4. **Generar los Triggers**(`trigger_generator.py`): Modifica el archivo CSV, para ello analiza todas las columnas en la cual haya presente un algoritmo y lo divide en pequeños grupos de movimientos llamados Triggers. 

5. **Generar PDF** (`generate_pdf.py`): Lee un archivo CSV con información sobre las imágenes y genera un documento PDF que incluye las imágenes procesadas y detalles adicionales.

6. **Generar Deck de Anki** (`anki_generator.py`): Pregunta al usuario que archivo CSV quiere que lea para generar el Deck de Anki, genera un Deck de Anki con los casos elegidos. En la parte frontal plantea el algoritmo para colocar el caso deseado, en la parte de atras se muestra la imagen del caso y debajo de ella se muestran los algoritmos para resolver dicho caso. 

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `Pillow`
  - `matplotlib`
  - `numpy`
  - `reportlab`
  - `shutil`
  - Anki

## Instrucciones de Uso

1. **Ejecutar Scripts**:
   - **Indicar flechas**: Ejecuta `arrow_indicator.py` para indicar que piezas se permutaran, se guardara en una colunna del archivo csv `DataBase.csv`.
   - **Descargar Imágenes**: Ejecuta `download_images.py` para descargar las imágenes necesarias, se guardaran en la carpeta `downloaded_images`.
   - **Generar algoritmo Set UP**: Ejecuta `set_up_generator.py` para añadir al archivo CSV `DataBase.csv` una columna que contenga un algoritmo Set Up para cada caso.
   - **Generar Triggers**: Ejecuta `trigger_generator.py` para modificar el archivo CSV `DataBase.csv` para que los algoritmos se dividan en Triggers.
   - **Generar PDF**: Ejecuta `generate_pdf.py` para generar el documento PDF final.
   - **Generar Deck de Anki** Ejecuta `anki_generator.py` para generar automaticamente un Deck de Anki. El script pregunta al usuario el nombre del Deck, genera un Deck de Anki con los casos elegidos. En la parte frontal plantea el algoritmo para colocar el caso deseado, en la parte de atras se muestra la imagen del caso y debajo de ella se muestran los algoritmos para resolver dicho caso. 

   ```bash
   python arrow_indicator.py
   python download_images.py
   python set_up_generator.py
   python trigger_generator.py
   python generate_pdf.py
   python anki_generator.py
    ```
2. **Usar Flashcards**:
    - **Instalar Anki** Si no tienes Anki instalado, descárgalo e instálalo desde [ankiweb.net](https://apps.ankiweb.net/)
    - **Instalar el Deck** Una vez hayas generado el Deck (`Nombre_elegido_por_el_usuario.apkg`), simplemente dale doble clic al archivo. Esto abrirá automáticamente Anki e importará el deck.
    - **Abrir Anki** Abre Anki y verás tu nuevo Deck en la lista de Decks. Selecciona el Deck para empezar a estudiar.
    - **Iniciar la Práctica** Al iniciar la práctica, aparecerá el algoritmo de Set Up en el anverso de la tarjeta (parte frontal), el cual deberás aplicar en el cubo Rubik. Presiona la barra espaciadora para ver la respuesta.
    - **Mostrar la Respuesta** Después de presionar la barra espaciadora, verás la imagen del caso y los algoritmos para resolverlo en el reverso de la tarjeta (parte trasera).
    - **Evaluar tu Conocimiento** Después de revisar la respuesta, Anki te preguntará si ya conoces el caso o si necesitas seguir practicándolo. Tendrás opciones como "Fácil", "Buena", "Difícil", o "Repetir". Selecciona la opción según tu nivel de confianza en ese caso. Se sincero, si no, no servira.
    - **Configurar el Número de Tarjetas por Día** Una vez termines tu sesión, puedes ajustar el número máximo de tarjetas que deseas repasar por día. Para hacerlo, selecciona tu Deck en la pantalla principal de Anki, haz clic en "Opciones" y ajusta el número de tarjetas nuevas y de repaso en la sección correspondiente.

    De esta forma, podrás mejorar tu conocimiento del método F2L mediante la repetición espaciada, asegurándote de dominar todos los casos a tu propio ritmo.


## Resultados:

1. Las imágenes procesadas se guardarán en la carpeta `downloaded_images`.

2. El documento PDF generado se guardará como `PLL_cases.pdf`.

3. Los Decks de Anki se guardaran como `Nombre_elegido_por_el_usuario.apkg`.

