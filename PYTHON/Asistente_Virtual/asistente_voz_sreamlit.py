


# https://pypi.org/project/SpeechRecognition/               pip install SpeechRecognition

# https://pypi.org/project/pyttsx3/                         pip install pyttsx3


# Terminal: cd PYTHON\Asistente_Virtual>streamlit run asistente_voz_sreamlit.py

# You can now view your Streamlit app in your browser.
#  Local URL: http://localhost:8501
#  Network URL: http://100.126.26.93:8501


import streamlit as st
import speech_recognition as sr
import pyttsx3

# Inicializar el reconocedor de voz
r = sr.Recognizer()
# Inicializar el sintetizador de voz
engine = pyttsx3.init()

def asistente_voz():
    """Función principal del asistente de voz."""

    # Configurar el micrófono
    with sr.Microphone() as source:
        # Ajustar sensibilidad del micrófono
        r.adjust_for_ambient_noise(source)
        # Escuchar la entrada de voz
        audio = r.listen(source)

    try:
        # Reconocer el texto hablado
        texto = r.recognize_google(audio)
        # Convertir texto a minúsculas
        texto = texto.lower()

        # Activar el asistente con la palabra clave "Alexa"
        if "alexa" in texto:
            # Eliminar la palabra clave "Alexa" del texto
            texto = texto.replace("alexa", "")

            # Buscar información en la web
            respuesta = buscar_en_web(texto)

            # Sintetizar la respuesta en voz alta
            engine.say(respuesta)
            engine.runAndWait()

    except sr.UnknownValueError:
        # Si no se reconoce el habla, mostrar un mensaje
        st.text("No se entendió lo que dijiste.")
    except sr.RequestError as e:
        # Si hay un error en la solicitud, mostrar un mensaje
        st.text(f"Ocurrió un error: {e}")

def buscar_en_web(texto):
    """Función para buscar información en la web."""
    # Reemplazar espacios por signos más para la URL
    texto_url = texto.replace(" ", "+")

    # Buscar resultados en Google
    url = f"https://www.google.com/search?q={texto_url}"
    # Obtener la página web
    response = requests.get(url)

    # Extraer el texto de la página web
    soup = BeautifulSoup(response.content, 'html.parser')
    resultados = soup.find_all('div', class_='g')

    # Formar la respuesta
    respuesta = f"Resultados para '{texto}':\n"
    for resultado in resultados:
        titulo = resultado.find('h3').a.text
        enlace = resultado.find('h3').a['href']
        respuesta += f"- {titulo}: {enlace}\n"

    return respuesta

# Interfaz gráfica con Streamlit
st.title("Asistente de Voz")

# Botón para activar el asistente
if st.button("Activar Alexa"):
    asistente_voz()


