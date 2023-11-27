
# APP config / renombrar tambien en settings.py / installed apps / miapp.apps.MiappConfig
from django.apps import AppConfig


class MiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miapp'
    verbose_name = "Dwn | APP | Web"
