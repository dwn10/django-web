# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd PYTHON/Conversor_de_Divisas > pip install streamlit request
#                                   > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import requests

# Título de la aplicación
st.title("Conversor de Divisas")

# Obtener la lista de divisas de la API
url = "https://api.exchangerate-api.com/v4/latest/USD"  # Puedes usar otra API si lo prefieres
response = requests.get(url)
currencies = response.json()['rates'].keys()

# Selección de divisas
col1, col2 = st.columns(2)
with col1:
  from_currency = st.selectbox("De:", currencies)
with col2:
  to_currency = st.selectbox("A:", currencies)

# Ingresar la cantidad a convertir
amount = st.number_input("Cantidad:", min_value=0.0)

# Realizar la conversión
if st.button("Convertir"):
  # Obtener la tasa de cambio de la API
  url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
  response = requests.get(url)
  exchange_rate = response.json()['rates'][to_currency]

  # Calcular la cantidad convertida
  converted_amount = amount * exchange_rate

  # Mostrar el resultado
  st.write(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")