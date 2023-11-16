from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q

# 1ro Crear views o rutas / luego 2 URL

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

# inicio / return: muestra x pantalla objs / def se crea URL
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

#------------------------------------------------
# crear formularios
def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        # validacion si el titulo es menor a 5 letras
        if len(title)<= 5:
            return HttpResponse("<h2>El titulo es muy corto</h2>")

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        # guardar en BD
        articulo.save()

        return HttpResponse(f"Articulo creado: <strong> {articulo.title} </strong> - {articulo.content}")
    
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

# crear articulo template form
def create_article(request):
    return render(request, 'create_article.html')
#------------------------------------------------

# mostrar datos de BD / id / pk Primary Key / title ="xxx" / try

def articulo(request):
    try:
        articulo = Article.objects.get(pk=2, public=True)
        return HttpResponse(f"articulo: <br/> {articulo.id}.) {articulo.title}")
    except:
        response = "<h1>Articulo no encontrado</h1>"
    return HttpResponse(response)

# actualizar registros
def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "peli del 2017"
    articulo.public = True

    # guardar en BD
    articulo.save()

    return HttpResponse(f"Articulo {articulo.id}.) editado: <br/><strong> {articulo.title}</strong>")

# listar todos los articulos all / otra variante .order_by :(id) / (-id): inverso /
# (-title)[:3]= limita muestra solo 3 obj /(id)[3:10]=mostrar del 3 al 10
def articulos(request):

    articulos = Article.objects.all().order_by('-id')


    # consultas con condiciones filter / lookup / title__ixact / id__gt=10 (id mayor a 10) / id__lt=10 (id menor a 10) / exclude
    """
    articulos = Article.objects.filter(
                                    title="3er articulo",
                                    ).exclude(
                                        public=False
                                    )
    """

    return render(request, 'articulos.html',{
    'articulos': articulos
})

# eliminar articulos
def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    # luego de borrar, redirigir a URL con nombre articulos
    return redirect('articulos')