from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

# Create your views here.
# MVC = Modelo Vista Controlador
# MVT = Modelo Vista Template


# layout
layout =("""
    <h1>Sitio web con django | Darwin Paz</h1>
    <hr/>
    <ul>
         <li>
         <a href="/inicio">Inicio</a>
         </li>

         <li>
         <a href="/hola-mundo">Hola Mundo</a>
         </li>

         <li>
         <a href="/pagina-test">Página web</a>
         </li>

         <li>
         <a href="/contacto">Contacto</a>
         </li>
    </ul>
    <hr/>
""")

# prueba de variables
year = 2023
hasta = range(year, 2051)

nombre = 'Darwin Paz'
lenguajes = ['JavaScript','Python', 'PHP', 'CSS']

# inicio
def index_test(request):
    return render(request, 'index.html',{
        'title': 'Inicio',
        'nombre' : nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

# hola mundo
def hola_mundo(request):
    return render(request, 'hola-mundo.html')

# pagina / redirigir

def pagina_test(request):
    return render(request, 'pagina-test.html',{
        'texto': 'respeta mmb...',
        'lista': ['uno','dos', 'tres']
    })

# def pagina(request, redirigir = 0):

    # if redirigir == 1:
        # return redirect('contacto', nombre="Darwin", apellidos="Paz")

        # return render(request, 'pagina-test.html')

# contacto
def contacto_test(request):
    return render(request, 'contacto.html')
    
# contacto / escribir parametros en url / muestra en web
# def contacto(request, nombre="", apellidos=""):

#    html = ""
#    if nombre and apellidos:
#        html += "<p>El nombre completo es: </p>"
#       html += f"<h3>{nombre} {apellidos}</h3>"

#    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

# crear articulos / importar /miapp.models/ Article
def crear_articulo(request, title, content, public):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    # guardar en BD
    articulo.save()

    return HttpResponse(f"Articulo creado: <strong> {articulo.title} </strong> - {articulo.content}")