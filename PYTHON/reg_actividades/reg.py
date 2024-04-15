# 1) https://pypi.org/project/streamlit/        pip install streamlit
# 2) https://pypi.org/project/panda/            pip install panda
# 3) https://pypi.org/project/DateTime/         pip install DateTime

# 4) Terminal: cd PYTHON/reg_actividades>streamlit run reg.py
# 5) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501


import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from fpdf import FPDF

# Configuración de la página de Streamlit
st.set_page_config(layout="wide")
st.title("Herramienta de registro de tiempos y creación de certificados")

# Función para iniciar sesión o crear una cuenta
def login_or_create_account():
    # Implementar la lógica de autenticación o creación de cuenta

# Función para obtener la hoja de horas diaria del usuario
def get_daily_timesheet(user, date):
    # Implementar la lógica para obtener la hoja de horas diaria del usuario y la fecha especificada
    # (por ejemplo, desde una base de datos o un archivo CSV)

# Función para generar el certificado de formación
def generate_training_certificate(user, date):
    # Implementar la lógica para generar el certificado de formación en formato PDF
    # utilizando la biblioteca FPDF
    # (incluir información del usuario, fecha, etc.)

# Función para guardar o imprimir el informe
def save_or_print_report(report_data, format="pdf"):
    if format == "pdf":
        # Guardar el informe en formato PDF
        pass
    elif format == "print":
        # Imprimir el informe
        pass
    else:
        raise ValueError(f"Formato de informe no válido: {format}")

# Función para editar un informe existente
def edit_report(report_id):
    # Implementar la lógica para editar un informe existente
    # (por ejemplo, modificar datos en una base de datos o un archivo CSV)

# Función para eliminar un informe existente
def delete_report(report_id):
    # Implementar la lógica para eliminar un informe existente
    # (por ejemplo, eliminar datos de una base de datos o un archivo CSV)

# Función para generar informes diarios
def generate_daily_reports():
    # Implementar la lógica para generar informes diarios para todos los usuarios
    # (por ejemplo, generar informes en formato PDF o imprimirlos)

# Iniciar sesión o crear cuenta
st.sidebar.header("Iniciar sesión / Crear cuenta")
if st.sidebar.button("Iniciar sesión"):
    login_or_create_account()
elif st.sidebar.button("Crear cuenta"):
    login_or_create_account()

# Seleccionar usuario y fecha
st.header("Seleccionar usuario y fecha")
user = st.selectbox("Usuario", ["Usuario 1", "Usuario 2", "Usuario 3"])
date = st.date_input("Fecha", value=datetime.date.today())

# Obtener hoja de horas diaria
timesheet_data = get_daily_timesheet(user, date)

# Mostrar hoja de horas diaria
st.header("Hoja de horas diaria")
st.table(timesheet_data)

# Generar certificado de formación
if st.button("Generar certificado de formación"):
    generate_training_certificate(user, date)

# Guardar o imprimir informe
if st.button("Guardar o imprimir informe"):
    report_format = st.radio("Formato de informe", ["PDF", "Imprimir"])
    save_or_print_report(timesheet_data, report_format)

# Editar informe
if st.button("Editar informe"):
    edit_report(report_id)  # Implementar la lógica para obtener el ID del informe

# Eliminar informe
if st.button("Eliminar informe"):
    delete_report(report_id)  # Implementar la lógica para obtener el ID del informe

# Generar informes diarios
if st.button("Generar informes diarios"):
    generate_daily_reports()