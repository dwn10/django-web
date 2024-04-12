# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 2) https://pypi.org/project/pybraille/      pip install pybraille
# 3) https://pypi.org/project/pyttsx4/        pip install pyttsx4
# 3) Terminal: Proyecto>streamlit run traductor_braille.py
# 4) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

import streamlit as st
from pybraille import Braille
from pyttsx3 import init as tts_init, speak as tts_speak

# Inicializar pyttsx3 (opcional)
tts = tts_init()

def convertir_a_braille(texto):
  braille_obj = Braille()
  braille_texto = braille_obj.convert(texto)
  return braille_texto

# st.title("Traductor de texto a braille")
# Configuración de la página web
st.set_page_config(page_title="Traductor de texto a braille", page_icon="🔎", layout="centered")
# Imagen
st.image("images/Cloud_Coding.png", use_column_width="auto")

texto_introducido = st.text_input("Introduce el texto a convertir")

if st.button("Convertir"):
  braille_texto = convertir_a_braille(texto_introducido)
  st.write(f"Código braille: {braille_texto}")

  # Reproducir el texto en voz alta (opcional)
  tts_speak(braille_texto)

  