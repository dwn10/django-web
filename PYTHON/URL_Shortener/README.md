## requerimientos

<ul>
	<li><a href="https://pypi.org/project/pyshorteners/">pyshorteners</a></li>
	<li><a href="https://pypi.org/project/streamlit/">streamlit</a></li>
	<li><a href="https://www.piliapp.com/facebook-symbols/">icons</a></li>
	
</ul>

## aplicación web simple que acorta URLs usando la librería pyshorteners.

## Funciones:
- `shorten_url(url):` Intenta acortar la URL dada usando `pyshorteners`. Si hay un error (por ejemplo, una URL inválida), muestra un mensaje de error y devuelve `None`. Si la operación es exitosa, devuelve la URL acortada.

## Configuración de Streamlit:
- Se configura el título de la página web como `"URL Shortener"`, el ícono de la página ("🌐") y el centrado del layout.

## Interfaz:
- Se muestra una imagen llamada `"www.png"` a lo ancho de la columna.
- Se muestra un título `"URL Shortener"`.
- Se crea un campo de texto donde el usuario puede ingresar una URL.
- Se crea un botón que dice "Generate new URL" `(Generar nueva URL)`.

## Comportamiento del botón:
- Al hacer clic en el botón, se llama a la función `shorten_url` con la URL ingresada por el usuario.
- Si la URL se acortó con éxito, se muestra el mensaje "URL shortened: " seguido de la URL acortada.