## requerimientos



<ul>
	<li><a href="https://pypi.org/project/qrcode/">QR Code</a></li>
	<li><a href="https://pypi.org/project/streamlit/">streamlit</a></li>
	<li><a href="https://www.piliapp.com/facebook-symbols/">icons</a></li>
</ul>

## aplicación web genera fácilmente códigos QR a partir de URL que ingresen en la interfaz.

## Resumen:

Este código de Python crea una aplicación web de Streamlit para generar códigos QR a partir de URL ingresadas por el usuario. He aquí un desglose de su funcionamiento:

## 1. Importaciones:

- `qrcode:` Biblioteca para generar códigos QR.
- `streamlit as st:` Biblioteca para crear interfaces web de Streamlit.

## 2. Nombre del archivo:

- `filename:` Almacena la ruta del archivo del código QR generado `("QR_Codes/qr_code.png")`.

## 3. Función generate_qr_code:

- Toma la URL y el nombre del archivo como parámetros.
- Crea un objeto `qrcode.QRCode` con las siguientes configuraciones:
  -- `version=1`: Nivel de complejidad del código QR (1 es el más básico).
  -- `error_correction=qrcode.constants.ERROR_CORRECT_L`: Nivel de corrección de errores (L es el más bajo).
  -- `box_size=10`: Tamaño de cada módulo del código QR.
  -- `border=4`: Ancho del borde del código QR.
- Agrega la URL a los datos del código QR `(qr.add_data(url))`.
- Genera el código QR `(qr.make(fit=True))`.
- Crea una imagen del código QR con colores `negro (relleno)` y `blanco (fondo)` `(img = qr.make_image(fill_color="black", back_color="white"))`.
- Guarda la imagen en el archivo especificado `(img.save(filename))`.

## 4. Aplicación Streamlit:

- Configura el título, el icono y el diseño de la página `(st.set_page_config)`.
- Muestra una imagen de fondo `(st.image("images/supports.JPG"))`.
- Crea un título para la aplicación `(st.title("Generador de códigos QR"))`.
- Permite al usuario ingresar una URL en un campo de texto `(url = st.text_input("Ingrese la URL"))`.
- Proporciona un botón para generar el código QR `(if st.button("Generar código QR"))`.
  -- Si se hace clic en el botón, se llama a la función `generate_qr_code` con la URL y el nombre del archivo.
  -- Muestra la imagen del código QR generado `(st.image(filename)`.
  -- Abre un cuadro de diálogo para descargar el código QR `(st.download_button)`.
