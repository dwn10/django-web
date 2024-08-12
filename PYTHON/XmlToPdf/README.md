# Herramienta web interactiva para procesar y descargar datos de archivos XML.

## Funcionalidades Principales:

<a href="https://github.com/dwn10/django-web/blob/main/PYTHON/XmlToPdf/XmlToPdf.gif"><img src="https://github.com/dwn10/django-web/blob/main/PYTHON/XmlToPdf/XmlToPdf.gif" style="height: 80%; width:80%;"/></a>

## Carga de archivo XML:

- Permite al usuario subir un archivo XML a través de un componente de carga de archivos.

## Procesamiento de XML:

- La función process_xml lee y analiza el archivo XML cargado.
- Extrae datos relevantes del XML y los organiza en un DataFrame de Pandas, lo que facilita su manipulación y visualización.
- Muestra los datos cargados en una tabla interactiva en la interfaz de Streamlit.

## Selección de filas:

- Permite al usuario seleccionar múltiples filas de los datos cargados utilizando un componente de selección múltiple.
- Impide la selección duplicada de filas.

## Descarga de datos:

## Ofrece dos opciones de descarga:

`XML:`

- Genera un nuevo archivo XML que contiene solo los datos de las filas seleccionadas y permite al usuario descargarlo.
  `PDF:`
- Genera un archivo PDF con los datos de las filas seleccionadas (el formato específico del PDF puede personalizarse) y permite al usuario descargarlo.
- Antes de generar y descargar los archivos, verifica que el usuario haya seleccionado al menos una fila.
