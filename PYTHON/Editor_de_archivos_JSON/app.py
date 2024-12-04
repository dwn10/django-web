# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd PYTHON/Editor_de_archivos_JSON > pip install streamlit json
#                                   > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import json
from io import StringIO  # Importa StringIO desde io

st.title("Editor de archivos JSON")

col1, col2 = st.columns(2)  # Divide la pantalla en dos columnas

with col1:
    st.subheader("Lector JSON")
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
    st.subheader("Editor JSON")
    if uploaded_file is not None:
        try:
            # Mostrar el JSON en un editor editable
            edited_data = st.text_area("Edita el JSON", json.dumps(data, indent=4), height=400)

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