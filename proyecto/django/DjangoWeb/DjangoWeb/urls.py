"""
URL configuration for DjangoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importar vistas
from miapp import views

# crear ruta url / nombre pag = URL a llamar / conecta de la tabla views / + nombre no es obligatorioS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_test, name="index"),

    path('inicio/', views.index_test, name="inicio"),
    path('hola-mundo/',views.hola_mundo, name="hola mundo"),
    path('pagina-test/', views.pagina_test, name="pagina"),
    # path('pagina-test/', views.pagina, name="pagina"),

    path('contacto/', views.contacto_test, name="contacto"),
    # path('contacto/<str:nombre>/', views.contacto, name="contacto"),
    # path('contacto/<str:nombre>/<str:apellidos>', views.contacto, name="contacto")

    # ingresar art por medio de URL
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),

    # mostrar articulo de BD
    path('articulo/', views.articulo, name="articulo"),

    # actualizar registros
    path('editar-articulo/<int:id>', views.editar_articulo),

    # cargar todos los articulos
    path('articulos/', views.articulos, name="articulos"),

    # eliminar articulo de BD
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),

    # crear articulo formulario
    path('create-article/', views.create_article, name="create"),

    # guardar articulo formulario
    path('save-article', views.save_article, name="save")
]
