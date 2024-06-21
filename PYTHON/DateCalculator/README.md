
## Calculador de Tiempo:

`>> IMG + VIDEO <<`

<a href=".\django-web\PYTHON\DateCalculator\readme-IMG\DataCalculator.gif"><img src=".\django-web\PYTHON\DateCalculator\readme-IMG\DataCalculator.gif" style="height: 80%; width:80%;"/></a>


-  Aplicación web interactiva utilizando la biblioteca Streamlit
que calcula la diferencia de tiempo entre una fecha introducida por el usuario y la fecha actual.

## Configuración Inicial:

- Configura el título de la página como `"Calculadora de Tiempo"` y ajusta el diseño.

## Entrada del Usuario:

Muestra un campo de entrada donde el usuario puede seleccionar una fecha.

## Botón "Calcular:

`Cuando el usuario hace clic en el botón:`

- Verificación de la Fecha: Comprueba si se ha introducido una fecha válida.
- Cálculo de Diferencias: Calcula la diferencia en años, meses, días y horas entre las dos fechas.
- Información Adicional: Determina el día de la semana de la fecha introducida y si fue un año bisiesto.
- Presentación de Resultados: Muestra los resultados calculados en un formato legible.
- Manejo de Errores: Si no se proporciona una fecha, se muestra un mensaje de advertencia.

## Función calculate_date_difference(input_date):

- Esta función toma la fecha de entrada y la fecha de hoy para calcular la diferencia.
- Devuelve los años de diferencia, meses, días, total de horas,
nombre del día de la semana, e información si es año bisiesto.