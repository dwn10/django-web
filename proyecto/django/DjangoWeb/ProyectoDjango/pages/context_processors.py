
# pag generada para llamar desde settings.py
from pages.models import Page

def get_pages(request):
    pages = Page.objects.values_list('id','title', 'slug') # consulta al BD

    return {
        'pages': pages
    }