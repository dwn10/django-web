# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd PYTHON/XmlToPdf > pip install streamlit pandas fpdf
#                                   > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from fpdf import FPDF
import io

def process_xml(xml_file):
    #--------------------------------
    # Leer y analizar el archivo XML
    #--------------------------------
    tree = ET.parse(xml_file)
    root = tree.getroot()
    #-----------------------------------------------------------------------------
    # Extraer datos relevantes del XML (esto dependerá de la estructura de tu XML)
    #-----------------------------------------------------------------------------
    data = []
    for child in root:
        row = {}
        for subchild in child:
            row[subchild.tag] = subchild.text
        data.append(row)

    return pd.DataFrame(data)

def create_xml_output(selected_data):
    #----------------------------------------
    # Crear un nuevo elemento raíz XML
    #----------------------------------------
    root = ET.Element('data')
    #----------------------------------------
    # Agregar los datos seleccionados al XML
    #----------------------------------------
    for row in selected_data:
        item = ET.SubElement(root, 'item')
        for key, value in row.items():
            ET.SubElement(item, key).text = str(value)

    #---------------------------------------------
    # Crear un árbol XML y devolverlo como string
    #---------------------------------------------
    tree = ET.ElementTree(root)
    output = io.BytesIO()
    tree.write(output, encoding='utf-8', xml_declaration=True)
    output.seek(0)
    return output

#---------------------------------------------
# Agregar los datos seleccionados al PDF
#---------------------------------------------
def create_pdf_output(selected_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    #---------------------------------------------
    # Obtener todas las claves únicas (nombres de columna)
    #---------------------------------------------
    all_keys = set()
    for row in selected_data:
        all_keys.update(row.keys())
    #---------------------------------------------
    # Ordenar las claves alfabéticamente
    #---------------------------------------------
    sorted_keys = sorted(all_keys)
    #---------------------------------------------
    # Calcular el ancho de cada columna (asumiendo un ancho máximo de página de 210 mm)
    #---------------------------------------------
    num_columns = len(sorted_keys)
    column_width = 210 / num_columns
    #---------------------------------------------
    # Imprimir encabezados de columna
    #---------------------------------------------
    for key in sorted_keys:
        pdf.cell(column_width, 10, txt=key, border=1, align='C')  # Centrar el texto en el encabezado
    pdf.ln()
    #---------------------------------------------
    # Imprimir datos en columnas
    #---------------------------------------------
    for row in selected_data:
        for key in sorted_keys:
            value = row.get(key, "")  # Obtener el valor o una cadena vacía si la clave no existe
            pdf.cell(column_width, 10, txt=str(value), border=1)
        pdf.ln()

    #----------------------------
    # Devolver el PDF como bytes
    #----------------------------
    output = io.BytesIO()
    pdf.output(dest='S').encode('latin-1')
    output.write(pdf.output(dest='S').encode('latin-1'))
    output.seek(0)
    return output

def main():
    #---------------------------------------------------------
    #---------------------------------------------------------
    # Configuración de la página / Título / icono / subtítulo
    #---------------------------------------------------------
    #---------------------------------------------------------
    st.set_page_config(
        page_title="Herramienta para procesar datos XML",
        page_icon="images/EC-IT-LOGO-1.png",
        layout="centered"
    )
    st.subheader("Herramienta para procesar datos XML.")

    xml_file = st.file_uploader("Cargar archivo", type="xml")

    if xml_file:
        df = process_xml(xml_file)
        st.subheader("Datos cargados")
        st.dataframe(df)

        #---------------------------------------------------------
        # Selección múltiple de filas (sin repetición)
        #---------------------------------------------------------
        selected_rows = st.multiselect("Seleccionar filas para el informe", options=range(len(df)), key="selected_rows")

        if st.button("Descargar XML"):
            if selected_rows:  # Verificar si se han seleccionado filas
                selected_data = df.iloc[selected_rows].to_dict('records')
                output = create_xml_output(selected_data)
                st.download_button("Descargar XML", output, "datos_seleccionados.xml", "text/xml")
            else:
                st.warning("Por favor, selecciona al menos una fila antes de descargar.")

        if st.button("Descargar PDF"):
            if selected_rows:  # Verificar si se han seleccionado filas
                selected_data = df.iloc[selected_rows].to_dict('records')
                output = create_pdf_output(selected_data)
                st.download_button("Descargar PDF", output, "datos_seleccionados.pdf", "application/pdf")
            else:
                st.warning("Por favor, selecciona al menos una fila antes de descargar.")

main()