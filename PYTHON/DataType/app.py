# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 3) Terminal: cd PYTHON/DataType > streamlit run app.py

# 4) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

import streamlit as st
from datetime import datetime, date, time
from decimal import Decimal
import ast      # Import ast for safer evaluation
import random   # Password generator
import string   # Password generator
import pyshorteners     # URL Shortener https://pypi.org/project/pyshorteners/   pip install pyshorteners
import qrcode           # https://pypi.org/project/qrcode/       pip install qrcode
from io import BytesIO  # qrcode


#--------------------------------
# Braille translation dictionary
#--------------------------------
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

#--------------------------------
#Page config
#--------------------------------
st.set_page_config(page_title="EC-IT Tools", page_icon="images/EC-IT-LOGO-1.png", layout="centered")
#st.image("images/binary-code-tunel.jpg")

#--------------------------------
# Option menu
#--------------------------------
selected_option = st.sidebar.radio(
    "🛠️Elige una herramienta:",
    ["Calculadora Básica",
        "Identificador de Tipos Datos",
        "Conversor a Binario",
        "Conversor de Texto a Hexadecimal",
        "Traductor a Braille",
        "Generador de Password",
        "Acortador de URL",
        "IMC - Calc. de Índice de Masa Corporal",
        "Calculador de Tiempo",
        "Generador de QR"]
)

#--------------------------------
# Calculator
#--------------------------------
if selected_option == "Calculadora Básica":
    st.subheader("Calculadora Básica")

    st.markdown(
        """
        <style>
        .stNumberInput {
            width: 52% !important; /* Set width to 30% */
            margin-bottom: 10px;  /* Add some spacing between elements */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    num1 = st.number_input("Primer número:")
    num2 = st.number_input("Segundo número:")
    operation = st.radio("Operación:", ["Suma (+)", "Resta (-)", "Multiplicación (*)", "División (/)"])

    if st.button("Calcular"):
        if operation == "Suma (+)":
            result = num1 + num2
        elif operation == "Resta (-)":
            result = num1 - num2
        elif operation == "Multiplicación (*)":
            result = num1 * num2
        elif operation == "División (/)":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: División por cero"
        else:
            result = "Operación no válida"  # Just in case

        # Display result with parity information
        if isinstance(result, (int, float)):
            parity = "par" if result % 2 == 0 else "impar"
            st.success(f"Resultado: {result} (número {parity})")
        else:
            st.success(f"Resultado: {result}")  # For errors or non-numeric results

#--------------------------------
# Type identifier
#--------------------------------
elif selected_option == "Identificador de Tipos Datos":
    st.subheader("Identificador de Tipos Datos")
    st.image("images/ec-it-tools-3.JPG", use_column_width=True)
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

#--------------------------------
# Binary converter
#--------------------------------
elif selected_option == "Conversor a Binario":
    st.subheader("Conversor a Binario")
    st.image("images/ec-it-tools-2.JPG", use_column_width=True)
    text = st.text_input("Ingresa un texto:")
    if text:
        binary_str = "".join(format(ord(char), '08b') for char in text)
        st.write(f"Texto en binario:")
        st.code(binary_str)

#--------------------------------
# Binary hexadecimal
#--------------------------------
elif selected_option == "Conversor de Texto a Hexadecimal":
    st.subheader("Conversor de Texto a Hexadecimal")
    st.image("images/ec-it-tools-3.JPG", use_column_width=True)
    input_text = st.text_input("Ingresa un texto:")
    if input_text:
        hex_output = "".join(format(ord(c), "02x") for c in input_text)
        st.write(f"Texto en hexadecimal:")
        st.code(hex_output)

#--------------------------------
# Braille translator
#--------------------------------
elif selected_option == "Traductor a Braille":
    st.subheader("Traductor a Braille")
    st.image("images/ec-it-tools-2.JPG", use_column_width=True)
    text = st.text_input("Ingresa un texto (solo letras minúsculas):").lower()
    if text:
        braille_text = "".join(braille_dict.get(char, '') for char in text)
        st.write(f"Texto en braille:")
        st.code(braille_text)

#--------------------------------
# Password generator
#--------------------------------
elif selected_option == "Generador de Password":
    st.subheader("Generador de Password")
    st.image("images/ec-it-tools-3.JPG", use_column_width=True)

    def generate_password(length=12):
        """Generates a strong random password."""
        characters = string.ascii_letters + string.digits + string.punctuation  # Include all character types
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    password_length = st.slider("Longitud de la contraseña:", min_value=8, max_value=32, value=12)  # Set default length to 12

    if st.button("Generar Password"):
        generated_password = generate_password(password_length)
        
        st.write(f"Contraseña generada:")
        st.code(generated_password)

#--------------------------------
# URL Shortener
#--------------------------------
elif selected_option == "Acortador de URL":
    st.subheader("Acortador de URL")
    st.image("images/ec-it-tools-2.JPG", use_column_width=True)

    url_to_shorten = st.text_input("Ingrese la URL:")

    if st.button("Acortar URL") and url_to_shorten:
        try:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(url_to_shorten)
            #st.success(f"URL acortada: {shortened_url}")
            st.write(f"URL acortada:")
            st.code(shortened_url)
        except Exception as e:
            st.error(f"Error al acortar la URL: {e}")

#--------------------------------
# BMI Calculator
#--------------------------------
elif selected_option == "IMC - Calc. de Índice de Masa Corporal":
    st.subheader("Calculadora de Índice de Masa Corporal (IMC)")
    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Peso 80(kg):", value=0)
    with col2:
        height = st.number_input("Altura 1,78(m):", value=0.0)

    if st.button("Calcular IMC"):
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.write(f"Tu IMC es: {bmi:.2f}")

            if bmi < 18.5:
                st.info("Bajo peso")
            elif 18.5 <= bmi < 25:
                st.success("Peso normal")
            elif 25 <= bmi < 30:
                st.warning("Sobrepeso")
            else:
                st.error("Obesidad")
        else:
            st.error("Por favor, ingrese valores válidos para peso y altura.")

#--------------------------------
# Time Calculator
#--------------------------------
elif selected_option == "Calculador de Tiempo":
    st.subheader("Calcula la diferencia horaria entre una fecha determinada y la fecha actual.")
    # Input date in a 50% width container
    input_container = st.container()
    with input_container:
        input_date_str = st.date_input("Introduce una fecha (AAAA-MM-DD):")
        input_date = input_date_str
        
    # Calculate button centered below the date input
    calculate_button = st.button("Calcular")

    # Display results only when button is clicked
    if calculate_button and input_date_str:
        def calculate_time_difference(input_date):
            """Calculate time difference between input_date and today."""
            today = date.today()

            # Calculate exact difference using datetime objects
            start_datetime = datetime.combine(input_date, time.min)
            end_datetime = datetime.combine(today, time.min)
            time_difference = end_datetime - start_datetime

            years_diff = time_difference.days // 365
            remaining_days = time_difference.days % 365

            months_diff = remaining_days // 30
            days_diff = remaining_days % 30

            total_hours = time_difference.total_seconds() / 3600

            # Day of the week and leap year
            day_names_es = {
                "Monday": "Lunes",
                "Tuesday": "Martes",
                "Wednesday": "Miércoles",
                "Thursday": "Jueves",
                "Friday": "Viernes",
                "Saturday": "Sábado",
                "Sunday": "Domingo",
            }
            day_of_week_es = day_names_es[input_date.strftime("%A")]
            is_leap_year = input_date.year % 4 == 0 and (input_date.year % 100 != 0 or input_date.year % 400 == 0)

            return years_diff, months_diff, days_diff, total_hours, day_of_week_es, is_leap_year

        years, months, days, hours, day_name, leap_year = calculate_time_difference(input_date)

        st.subheader(f"Diferencia de tiempo entre {input_date_str} & {date.today()}:")
        st.write(f"Años: {years}")
        st.write(f"Mese(s): {months}")
        st.write(f"Día(s): {days}")
        st.write(f"Total Horas: {hours:.2f}")  # Rounded to 2 decimal places

        st.write(f"Día de la semana: {day_name}")
        st.write(f"Fue un año bisiesto: {'Sí' if leap_year else 'No'}")
    else:
        # Display a message if the button hasn't been clicked yet
        st.info("Haz clic en 'Calcular' para obtener la diferencia de tiempo.")
        
#--------------------------------
# QR code generator
#--------------------------------
elif selected_option == "Generador de QR":
    st.subheader("Generador de Código QR")
    url = st.text_input("Ingrese un texto o URL:")

    if st.button("Generar QR"):
        if url:
            filename = "qr_code.png"

            # QR Code generation
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            buffered = BytesIO()
            img.save(buffered, format="PNG")

            st.image(buffered, caption="Código QR Generado", use_column_width=True)

            # Download button
            st.download_button(label="Descargar QR", data=buffered.getvalue(), file_name="qr_code.png", mime="image/png")
        else:
            st.warning("Por favor, ingrese un texto o URL.")