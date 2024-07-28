# App web interactiva utilizando Streamlit para mostrar una lista de Pokémon.

<a href="https://github.com/dwn10/django-web/blob/main/PYTHON/DataSet/DataSet.gif"><img src="https://github.com/dwn10/django-web/blob/main/PYTHON/DataSet/DataSet.gif" style="height: 80%; width:80%;"/></a>

## Funcionalidades Principales:

- `Selección de Pokémon:` Un deslizador permite al usuario elegir cuántos Pokémon desea ver (hasta 150).

- `Obtención de Datos:` El código recupera información de cada Pokémon seleccionado desde la PokeAPI, incluyendo nombre, imagen y tipos.

- `Visualización:` Los Pokémon se muestran en una tabla con tres columnas: ID, imagen y nombre/tipos.

- `Generación de PDF:` Un botón permite descargar la lista de Pokémon en formato PDF.

## Librerías Utilizadas:`

- `streamlit:` Para crear la interfaz web interactiva.
- `requests:` Para realizar peticiones HTTP a la PokeAPI y obtener los datos.
- `fpdf:` Para generar el archivo PDF.

## Flujo de Trabajo:

- El usuario selecciona el número de Pokémon a mostrar.
- La aplicación consulta la PokeAPI para obtener los datos de los Pokémon seleccionados.
- Se crea un diseño de tabla en la interfaz para mostrar los datos de cada Pokémon.
- Opcionalmente, el usuario puede descargar un PDF con la lista de Pokémon (sin imágenes en esta versión).
