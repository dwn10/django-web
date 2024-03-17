
# 1) https://pypi.org/project/pyshorteners/   pip install pyshorteners
# 2) https://pypi.org/project/streamlit/      pip install streamlit
# 3) Terminal: Proyecto>streamlit run url_shortener.py
# 4) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

import pyshorteners
import streamlit as st

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except ValueError as e:
        st.error("Invalid URL. Please enter a valid URL.")
        return None

# Configuración de la página web
st.set_page_config(page_title="URL Shortener", page_icon="🌐", layout="centered")

# Imagen
st.image("images/Cloud_Coding.png", use_column_width="auto")

# Título
st.title("URL Shortener")

# Input para la URL
url = st.text_input("Enter the URL")

# Botón para generar la URL acortada
if st.button("Generate new URL"):
    shortened_url = shorten_url(url)
    if shortened_url:
        st.write("URL shortened: ", shortened_url)
