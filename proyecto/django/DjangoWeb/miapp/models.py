
# BD
from django.db import models

# Create your models here.

# Articulo / verbose_name traduce directo en la Panel de control
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Título")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(default='null', verbose_name = "Miniatura", upload_to = "articles")
    public = models.BooleanField(verbose_name = "Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Editado")

    # Ordenar en BD plural / singular
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

        ordering = ['-id']

    # imprimir y mostrar en panel de control
    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.title} {public}"
    

# Categoria
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"