# 1) https://pypi.org/project/streamlit/      pip install streamlit

# 2) Terminal: cd PYTHON/DataSet > streamlit run app.py


# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import streamlit as st
import requests         # pip install requests
from fpdf import FPDF   # pip install fpdf



st.title("Lista de Pokémon")

# Slider para seleccionar el número de Pokémon
num_pokemons = st.slider("Número de Pokémon a mostrar:", 1, 151, 10)  # Valor por defecto: 10

# Función para obtener información de un Pokémon
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()
    return {
        "name": data["name"],
        "image": data["sprites"]["front_default"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

# Función para generar el PDF
def create_pdf(pokemon_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for pokemon in pokemon_list:
        pdf.cell(0, 10, f"#{pokemon['id']}: {pokemon['name'].capitalize()}", ln=True)
        pdf.cell(0, 10, f"Types: {', '.join(pokemon['types'])}", ln=True)
        # Agregar imagen (opcional, requiere más configuración)
        # pdf.image(pokemon['image'], x=10, y=pdf.get_y() + 5, w=30)
        pdf.ln(10)  # Espacio entre Pokémon

    return pdf.output(dest='S').encode('latin-1')  # Salida en bytes

# Mostrar la lista de Pokémon (hasta el número seleccionado)
pokemon_list = []  # Lista para almacenar los datos de los Pokémon
for pokemon_id in range(1, num_pokemons + 1):
    pokemon_data = get_pokemon_data(pokemon_id)
    pokemon_data["id"] = pokemon_id  # Agregar el ID al diccionario
    pokemon_list.append(pokemon_data)

    # Crear una fila para cada Pokémon
    col1, col2, col3 = st.columns([1, 2, 2])

    # Columna 1: ID
    with col1:
        st.write(f"#{pokemon_id}")

    # Columna 2: Imagen
    with col2:
        st.image(pokemon_data["image"], caption=pokemon_data["name"], width=100)

    # Columna 3: Nombre y tipos
    with col3:
        st.write(f"**{pokemon_data['name'].capitalize()}**")
        st.write(", ".join(pokemon_data["types"]))

# Botón para descargar el PDF
if st.button("Descargar PDF"):
    pdf_bytes = create_pdf(pokemon_list)
    st.download_button(
        label="Descargar Lista de Pokémon",
        data=pdf_bytes,
        file_name="pokemon_list.pdf",
        mime="application/pdf",
    )
