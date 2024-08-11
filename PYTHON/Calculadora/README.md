# Calculadora básica con historial usando la biblioteca Streamlit en Python.

<a href="https://github.com/dwn10/django-web/blob/main/PYTHON/Calculadora/CalStr.gif"><img src="https://github.com/dwn10/django-web/blob/main/PYTHON/Calculadora/CalStr.gif" style="height: 60%; width:60%;"/></a>

## Funcionalidades:

## Diseño:

- Utiliza `st.columns` para organizar los botones de la calculadora en una cuadrícula de 4 columnas.
- Muestra el resultado del cálculo en un campo de texto de solo lectura.
- Presenta un historial de cálculos en una tabla con dos columnas: `"NR"` (número de historial) y `"Resultado"`.

## Lógica:

- `append_to_result:` Agrega el valor del botón presionado a la expresión actual.

- Permite al usuario ingresar una expresión matemática haciendo clic en los botones.
- Cuando se presiona el botón `"="`, evalúa la expresión ingresada y muestra el resultado.
- Almacena cada cálculo realizado `(expresión y resultado)` en un historial.
- El botón `"AC"` borra tanto el campo de entrada como el historial de cálculos.

`Clear_result:` Limpia el campo de entrada y el historial de cálculos.

`Estado de la sesión:`

- Utiliza el estado de sesión `(st.session_state)` para almacenar el resultado actual y el historial de cálculos, lo que permite que la - aplicación mantenga la información entre interacciones del usuario.
- La función `eval()` se utiliza para evaluar las expresiones matemáticas ingresadas por el usuario.
- La tabla de historial se actualiza automáticamente cada vez que se realiza un nuevo cálculo.
