import requests # python3 -m pip install requests beautifulsoup4
from bs4 import BeautifulSoup

# Definir la URL de la página web
url = "https://web.arbeitsagentur...."

# Enviar una solicitud GET a la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página web
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer los datos de las ofertas de trabajo
    ofertas_trabajo = soup.find_all('article', class_='amt-card')

    for oferta_trabajo in ofertas_trabajo:
        # Extraer el título de la oferta de trabajo
        titulo = oferta_trabajo.find('h2', class_='amt-card__title').text.strip()

        # Extraer la profesión de la oferta de trabajo
        profesion = oferta_trabajo.find('span', class_='amt-card__subtitle').text.strip()

        # Extraer la ubicación de la oferta de trabajo
        ubicacion = oferta_trabajo.find('span', class_='amt-card__location').text.strip()

        # Imprimir los datos extraídos
        print(f"Título: {titulo}")
        print(f"Profesión: {profesion}")
        print(f"Ubicación: {ubicacion}")
        print("-----------------------------------")
else:
    print("Error al acceder a la página web")

