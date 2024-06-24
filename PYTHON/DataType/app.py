# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 3) Terminal: cd PYTHON/DataType > streamlit run app.py

# 4) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

import streamlit as st
from datetime import datetime, date, time
from decimal import Decimal
import ast  # Import ast for safer evaluation

# Braille translation dictionary
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' ',  # Space
    '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢',
    '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', '0': '⠴',
    '.': '⠄', ',': '⠂', ';': '⠆', ':': '⠒', '?': '⠦',
    '!': '⠖', '-': '⠤', '_': ' underscore ', '+': ' plus ',
    '=': ' equals ', '(': ' open parenthesis ', ')': ' close parenthesis ',
    '[': ' open bracket ', ']': ' close bracket ',
    '{': ' open brace ', '}': ' close brace ',
    '<': ' less than ', '>': ' greater than ',
    '/': ' slash ', '\\': ' backslash ',
    '|': ' vertical bar ', '*': ' asterisk ',
    '#': ' number sign ', '$': ' dollar sign ',
    '%': ' percent sign ', '@': ' at sign ',
    '^': ' caret ', '&': ' ampersand ',
    '~': ' tilde '
}

# Option menu
selected_option = st.sidebar.selectbox(
    "Elige una herramienta:",
    ["Calculadora Básica", "Identificador de Tipos Datos", "Conversor a Binario", "Conversor de Texto a Hexadecimal", "Traductor a Braille"]
)

# Calculator
if selected_option == "Calculadora Básica":
    st.subheader("Calculadora Básica")
    num1 = st.number_input("Número 1:")
    num2 = st.number_input("Número 2:")
    operation = st.selectbox("Operación:", ["+", "-", "*", "/"])

    if st.button("Calcular"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: División por cero"
        st.success(f"Resultado: {result}")

# Type identifier
elif selected_option == "Identificador de Tipos Datos":
    st.subheader("Identificador de Tipos Datos")
    data_str = st.text_input("Ingresa un valor:")  # Get input as a string

    if data_str:
        try:
            # Attempt to directly convert to date or time
            try:
                data = date.fromisoformat(data_str)
            except ValueError:
                try:
                    data = time.fromisoformat(data_str)
                except ValueError:
                    # If not date or time, use ast.literal_eval for other types
                    data = ast.literal_eval(data_str)

            data_type = type(data).__name__

            # User-friendly type mapping (enhanced)
            type_mapping = {
                "str": "str: Cadena de texto (e.g., 'hola', 'mundo')",
                "int": "int: Número entero (e.g., 123, 4567)",
                "float": "float: Número de punto flotante (e.g., 3.14, 2.718)",
                "Decimal": "Decimal: Número decimal de alta precisión",
                "bool": "bool: Valor booleano (True/False)",
                "list": "list: Lista (e.g., [1, 2, 3], ['a', 'b'])",
                "tuple": "tuple: Tupla (lista inmutable) (e.g., (1, 2), ('x', 'y'))",
                "dict": "dict: Diccionario (e.g., {'nombre': 'Juan', 'edad': 30})",
                "set": "set: Conjunto (e.g., {1, 2, 3}, {'a', 'b', 'c'})",
                "NoneType": "NoneType: Valor nulo (None)",
                "date": "date: Fecha (e.g., 1980-08-23)",
                "time": "time: Hora (e.g., 12:20:00)"
            }

            st.write(type_mapping.get(data_type, f"Tipo de dato desconocido: {data_type}"))

            
        except (ValueError, SyntaxError):
            st.error("Entrada no válida. Por favor, ingrese un valor válido (e.g., 'Hola', 123, 3.14, True, [1, 2, 3], {'a': 1}, None, 2024-08-23, 12:20:00, or 3 + 4j).)")


# Binary converter
elif selected_option == "Conversor a Binario":
    st.subheader("Conversor a Binario")
    text = st.text_input("Ingresa un texto:")
    if text:
        binary_str = "".join(format(ord(char), '08b') for char in text)
        st.write(f"Texto en binario:")
        st.code(binary_str)

# Binary hexadecimal
elif selected_option == "Conversor de Texto a Hexadecimal":
    st.header("Conversor de Texto a Hexadecimal")
    input_text = st.text_input("Introduce texto:")
    if input_text:
        hex_output = "".join(format(ord(c), "02x") for c in input_text)
        st.write(f"Texto en hexadecimal:")
        st.code(hex_output)

# Braille translator
elif selected_option == "Traductor a Braille":
    st.subheader("Traductor a Braille")
    text = st.text_input("Ingresa un texto (solo letras minúsculas):").lower()
    if text:
        braille_text = "".join(braille_dict.get(char, '') for char in text)
        st.write(f"Texto en braille:")
        st.code(braille_text)

