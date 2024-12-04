# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 2) Terminal: cd PYTHON/DataType > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

import streamlit as st
from datetime import datetime, date, time
from decimal import Decimal
import ast                                  # Import ast for safer evaluation
import random                               # Password generator
import string                               # Password generator
import pyshorteners                         # URL Shortener https://pypi.org/project/pyshorteners/   pip install pyshorteners
import qrcode                               # https://pypi.org/project/qrcode/       pip install qrcode
from io import BytesIO                      # qrcode
from datetime import date, datetime, time   # Calculadora de tiempo
import time                                 # Calculadora de tiempo
import simpleaudio as sa                    # Temporizador / https://pypi.org/project/simpleaudio/  / pip install simpleaudio
import requests                             # Conversor de Divisas
import json                                 # Editor de archivos JSON
from io import StringIO                     # Editor de archivos JSON

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
        "Conversor a Binario",
        "Conversor de Texto a Hexadecimal",
        "Traductor a Braille",
        "Generador de Password",
        "Acortador de URL",
        "IMC - Calc. de Índice de Masa Corporal",
        "Calculador de Fechas",
        "Generador de QR",
        "Conversor de Temperatura",
        "Calculadora de Tiempo",
        "Temporizador",
        "Conversor de Divisas",
        "Editor de archivos JSON"]
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
# Binary converter
#--------------------------------
elif selected_option == "Conversor a Binario":
    st.subheader("Conversor a Binario")
    st.image("images/ec-it-tools-2.JPG", use_container_width=True)
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
    st.image("images/ec-it-tools-3.JPG", use_container_width=True)
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
    st.image("images/ec-it-tools-2.JPG", use_container_width=True)
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
    st.image("images/ec-it-tools-3.JPG", use_container_width=True)

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
    st.image("images/ec-it-tools-2.JPG", use_container_width=True)

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
# Calculador de Fechas
#--------------------------------
elif selected_option == "Calculador de Fechas":
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
            start_datetime = datetime.combine(input_date, time.min)  # Usa time.min 
            end_datetime = datetime.combine(today, time.min)  # Usa time.min
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

            # Ajustar tamaño de la imagen
            st.image(buffered, caption="Código QR Generado", width=260)

            # Download button
            st.download_button(label="Descargar QR", data=buffered.getvalue(), file_name="qr_code.png", mime="image/png")
        else:
            st.warning("Por favor, ingrese un texto o URL.")

#--------------------------------
# Converter Celsius - Fahrenheit
#--------------------------------
elif selected_option == "Conversor de Temperatura":
    st.subheader("Conversor de Temperatura")

# Style the input field to be 50% wide
    st.markdown(
        """
        <style>
        .stNumberInput > div > div > input {
            width: 50% !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    col1, col2 = st.columns(2)

    with col1:
        temp_input = st.number_input("Temperatura:")
    with col2:
        unit_input = st.radio("Unidad:", ["Celsius", "Fahrenheit"])

    if st.button("Convertir"):
        if unit_input == "Celsius":
            result = (temp_input * 9/5) + 32
            st.write(f"{temp_input}°C equivalen a {result:.2f}°F")
        else:
            result = (temp_input - 32) * 5/9
            st.write(f"{temp_input}°F equivalen a {result:.2f}°C")

#--------------------------------
# Calculadora de tiempo
#--------------------------------
elif selected_option == "Calculadora de Tiempo":
    st.subheader("Calculadora de Tiempo")
    st.write("Ingresa tiempos en formato HH:MM")

    # Entrada de datos (sin segundos)
    col1, col2 = st.columns(2)
    with col1:
        horas1 = st.number_input("Horas:", min_value=0, step=1)
    with col2:
        minutos1 = st.number_input("Minutos:", min_value=0, max_value=59, step=1)

    col1, col2 = st.columns(2)
    with col1:
        horas2 = st.number_input("Horas:", min_value=0, step=1, key="horas2")
    with col2:
        minutos2 = st.number_input("Minutos:", min_value=0, max_value=59, step=1, key="minutos2")

    # Operación seleccionada (solo suma y resta)
    operacion = st.radio("Selecciona una operación:", ["Suma (+)", "Resta (-)"])

    # Cálculo y resultado (sin segundos)
    if st.button("Calcular"):
        tiempo1_minutos = horas1 * 60 + minutos1
        tiempo2_minutos = horas2 * 60 + minutos2

        if operacion == "Suma (+)":
            resultado_minutos = tiempo1_minutos + tiempo2_minutos
        else:  # "Resta (-)"
            resultado_minutos = tiempo1_minutos - tiempo2_minutos

        resultado_horas = resultado_minutos // 60
        resultado_minutos = resultado_minutos % 60

        st.success(f"Resultado: {resultado_horas:02}:{resultado_minutos:02}")

#--------------------------------
# Temporizador
#--------------------------------
elif selected_option == "Temporizador":
    st.subheader("Temporizador")
    st.write("Ingresa el tiempo en HH-MM-SS ")

    # Entrada de tiempo (horas, minutos, segundos) con validaciones
    col1, col2, col3 = st.columns(3)
    with col1:
        horas = st.number_input("Horas:", min_value=0, step=1)
    with col2:
        minutos = st.number_input("Minutos:", min_value=0, max_value=59, step=1)
    with col3:
        segundos = st.number_input("Segundos:", min_value=0, max_value=59, step=1)
    
    # Validación de entrada
    if horas == 0 and minutos == 0 and segundos == 0:
        st.warning("Ingresa un tiempo válido.")
    else:
        # Cálculo del tiempo total en segundos
        tiempo_total = horas * 3600 + minutos * 60 + segundos

        # Variable de estado para controlar el temporizador
        if "running" not in st.session_state:
            st.session_state.running = False

        # Botón para iniciar/pausar/reanudar
        if st.button("Iniciar/Cancelar"):
            st.session_state.running = not st.session_state.running  # Cambiar el estado

        # Placeholder para el conteo regresivo
        placeholder = st.empty()

        # Conteo regresivo
        while st.session_state.running and tiempo_total > 0:
            horas_restantes = tiempo_total // 3600
            minutos_restantes = (tiempo_total % 3600) // 60
            segundos_restantes = tiempo_total % 60
            placeholder.text(f"Tiempo restante: {horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}")
            time.sleep(1)
            tiempo_total -= 1

        # Alarma al finalizar
        if tiempo_total == 0 and st.session_state.running:  # Corrección: sonar la alarma cuando el temporizador está corriendo
            wave_obj = sa.WaveObject.from_wave_file("audio/alarm.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
            placeholder.text("¡Tiempo terminado!")
            st.session_state.running = False # Reiniciar el estado

#--------------------------------
# Conversor de Divisas
#--------------------------------

elif selected_option == "Conversor de Divisas":
    st.subheader("Conversor de Divisas en tiempo real")

    # Obtener la lista de divisas de la API
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    currencies = response.json()['rates'].keys()

    # Obtener los valores unitarios actuales
    eur_value = response.json()['rates']['EUR']

    # Mostrar los valores unitarios
    st.write(f"Valor actual de 1 EUR: {eur_value:.4f} USD")

    st.image("images/ec-it-tools-3.JPG", use_container_width=True)

    # Ajustar el ancho de las columnas
    col1, col2, col3, col4 = st.columns([1.5, 1.5, 3, 4])

    with col1:
        from_currency = st.selectbox("De:", currencies, index=list(currencies).index("EUR"))

    with col2:
        to_currency = st.selectbox("A:", currencies, index=list(currencies).index("USD"))

    with col3:
        amount = st.number_input("Cantidad:", min_value=0.0)

    with col4:
        if st.button("Convertir"):
            # Obtener la tasa de cambio de la API
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            exchange_rate = response.json()['rates'][to_currency]

            # Calcular la cantidad convertida
            converted_amount = amount * exchange_rate

            # Mostrar el resultado
            st.markdown(f"{amount} {from_currency} = **{converted_amount:.2f} {to_currency}**")
        
#--------------------------------
# Editor de archivos JSON
#--------------------------------

elif selected_option == "Editor de archivos JSON":
    st.header("Editor de archivos JSON")

    col1, col2 = st.columns(2)  # Divide la pantalla en dos columnas

    with col1:
        uploaded_file = st.file_uploader("Selecciona un archivo JSON", type="json")

        if uploaded_file is not None:
            # Leer el archivo como string
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            string_data = stringio.read()

            try:
                data = json.loads(string_data)
                st.json(data)  # Mostrar el JSON original en la columna izquierda
            except json.JSONDecodeError:
                st.error("Archivo JSON inválido")

    with col2:
        if uploaded_file is not None:
            try:
                # Mostrar el JSON en un editor editable
                edited_data = st.text_area("Editar JSON", json.dumps(data, indent=4), height=400)

                # Convertir el JSON editado a un objeto Python
                try:
                    edited_data = json.loads(edited_data)
                except json.JSONDecodeError:
                    st.error("JSON inválido en el editor")

                # Botón para descargar el JSON editado
                st.download_button(
                    label="Descargar JSON editado",
                    data=json.dumps(edited_data, indent=4),
                    file_name="data.json",
                    mime="application/json",
                )

            except json.JSONDecodeError:
                st.error("Archivo JSON inválido")