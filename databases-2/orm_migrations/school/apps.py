from django.apps import AppConfig
from django.db.models import BigAutoField


class SchoolConfig(AppConfig):
    name = 'school'
    verbose_name = 'Школа'
    default_auto_field = 'django.db.models.AutoField'
