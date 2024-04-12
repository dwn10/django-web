# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 2) https://pypi.org/project/requests/       python -m pip install requests
# 3) https://pypi.org/project/bs4/            pip install bs4

# 4) Terminal: Proyecto>streamlit run buscador_isbn.py
# 5) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501


import streamlit as st
import requests
from bs4 import BeautifulSoup

# Función para buscar por ISBN
def buscar_por_isbn(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos:
        libro = datos["ISBN:" + isbn]
        titulo = libro["title"]
        autores = libro["authors"]
        imagen = libro["cover"]["medium"]
        st.image(imagen)
        st.title(titulo)
        st.write("Autores:", ", ".join(autores))
    else:
        st.error("ISBN no encontrado")

# Función para buscar por título
def buscar_por_titulo(titulo):
    url = f"https://openlibrary.org/api/books?q={titulo}&jscmd=data&format=json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos:
        libros = datos["docs"]
        for libro in libros:
            isbn = libro["isbn"][0]
            buscar_por_isbn(isbn)
    else:
        st.error("Título no encontrado")

# Interfaz de usuario
# st.title("Buscador de ISBN")
# Configuración de la página web
st.set_page_config(page_title="Buscador de ISBN", page_icon="🔎", layout="centered")
# Imagen
st.image("images/Cloud_Coding.png", use_column_width="auto")

opcion = st.selectbox("¿Cómo desea buscar?", ("Por ISBN", "Por título"))

if opcion == "Por ISBN":
    isbn = st.text_input("Ingrese el ISBN del libro")
    if isbn:
        buscar_por_isbn(isbn)
else:
    titulo = st.text_input("Ingrese el título del libro")
    if titulo:
        buscar_por_titulo(titulo)

# Mostrar mensaje de ayuda
st.markdown("""
**Ayuda:**

* Introduzca el ISBN del libro que desea buscar.
* Haga clic en el botón "Buscar".
* Se mostrarán los detalles del libro, incluyendo la portada (si está disponible).
""")