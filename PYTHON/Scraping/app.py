# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 2) https://pypi.org/project/pybraille/      pip install pybraille
# 3) https://pypi.org/project/pyttsx4/        pip install pyttsx4
# 3) Terminal: Proyecto>streamlit run app.py
# 4) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501



import streamlit as st
from bs4 import BeautifulSoup
import requests

def extraer_datos(url):
  """
  Extrae el título y el autor de una página web.

  Args:
    url: La URL de la página web.

  Returns:
    Un diccionario con el título y el autor.
  """
  # Obtener la respuesta HTML
  response = requests.get(url)

  # Parsear el HTML
  soup = BeautifulSoup(response.content, "html.parser")

  # Extraer el título
  titulo = soup.find("title").text

  # Extraer el autor
  autor = soup.find("meta", name="author").get("content")

  # Devolver un diccionario con los datos
  return {"titulo": titulo, "autor": autor}


# Título de la aplicación
st.title("Scrapper de datos")

# Introducir la URL
url = st.text_input("Introduzca la URL de la página web")

# Botón para extraer datos
if st.button("Extraer datos"):
  # Extraer los datos
  datos = extraer_datos(url)

  # Mostrar los datos
  st.write("**Título:**", datos["titulo"])
  st.write("**Autor:**", datos["autor"])

  # Descargar datos a CSV
  st.download_button("Descargar datos", data=str(datos).encode("utf-8"), file_name="datos.csv")