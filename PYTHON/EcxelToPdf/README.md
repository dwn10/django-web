# Generador de informes

## App permite generar informes en formato Word `(.docx)` a partir de datos `(.xlsx o .csv)` cargados por el usuario.

<a href="https://github.com/dwn10/django-web/blob/main/PYTHON/EcxelToPdf/generador-de-informes.gif"><img src="https://github.com/dwn10/django-web/blob/main/PYTHON/EcxelToPdf/generador-de-informes.gif" style="height: 80%; width:80%;"/></a>

## El usuario puede:

`Cargar una plantilla Word:`

- Esta plantilla servirá como base para el informe final, y puede contener marcadores de posición `(placeholders)` como `{{nombre}}` para ser reemplazados con datos específicos.

`Cargar un archivo de datos (Excel o CSV):`

- Los datos de este archivo se utilizarán para completar los marcadores de posición en la plantilla y, opcionalmente, generar un gráfico chart.

`Seleccionar una fila de datos:`

- Si el archivo de datos contiene varias filas, el usuario puede elegir cuál utilizar para generar el informe.

`Generar un gráfico (opcional):`

- El usuario puede optar por incluir un gráfico de barras en el informe, especificando el título, las columnas para los ejes `X `e `Y`, y las etiquetas.

`Generar el informe:`

- Al hacer clic en el botón `"Generar Informe"`, el código procesa la plantilla, reemplaza los marcadores de posición con los datos seleccionados, inserta el gráfico `(si se solicitó)` y proporciona un `botón para descargar` el informe generado.

`Comentarios:`

- `Funcionalidad clara y útil:`

  - El código ofrece una forma práctica de automatizar la creación de informes, especialmente cuando se deben generar informes similares de forma repetida con datos variables.

- `Flexibilidad:`

  - Permite utilizar plantillas Word personalizadas y manejar datos tanto en formato Excel como CSV.

- `Visualización de datos:`
  - La opción de incluir gráficos mejora la presentación de la información en los informes.
