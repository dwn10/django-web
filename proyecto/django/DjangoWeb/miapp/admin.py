from django.contrib import admin
from .models import Article, Category


# Register your models here / con esto muestra estas carpetas en  Dashbord de admin

class ArticleAdmin(admin.ModelAdmin): # campos solo de lectura
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# configur titulo de Panel
title = "Django Web - Darwin Paz"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"
