# 1) https://pypi.org/project/streamlit/      pip install streamlit
# 3) Terminal: cd PYTHON/DateCalculator > streamlit run app.py

# 4) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

import streamlit as st
from datetime import datetime, date

def calculate_date_difference(input_date):
    today = date.today()
    years_diff = today.year - input_date.year
    months_diff = today.month - input_date.month
    days_diff = today.day - input_date.day

    if days_diff < 0:
        months_diff -= 1
        days_diff += input_date.replace(month=input_date.month % 12 + 1, day=1).day - 1

    if months_diff < 0:
        years_diff -= 1
        months_diff += 12

    total_hours = (today - input_date).total_seconds() / 3600

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

#Page config
st.set_page_config(page_title="Calculadora de Tiempo", page_icon="readme-IMG/EC-IT-LOGO-1.png", layout="centered")
st.image("readme-IMG/binary-code-tunel.jpg")
st.title("Calculadora de Tiempo")
st.markdown("Calcula la diferencia horaria entre una fecha determinada y la fecha actual.")

# Create two columns with the first one taking up 50% of the width
col1, col2 = st.columns([1, 1])

# Place the date input widget in the first column
with col1:
    input_date_str = st.date_input("Introduce una fecha (AAAA-MM-DD):")
    input_date = input_date_str

# Button to trigger calculation
if st.button("Calcular"):
    if input_date_str:
        years_diff, months_diff, days_diff, total_hours, day_of_week_es, is_leap_year = calculate_date_difference(input_date_str)

        st.subheader(f"Diferencia de tiempo entre {input_date_str} & {date.today()}:")
        st.write(f"Años: {years_diff}")
        st.write(f"Mese(s): {months_diff}")
        st.write(f"Día(s): {days_diff}")
        st.write(f"Total Horas: {total_hours:.2f}")

        st.write(f"Día de la semana: {day_of_week_es}")
        st.write(f"Fue un año bisiesto: {'Sí' if is_leap_year else 'No'}")
    else:
        st.warning("Por favor, introduce una fecha.")

