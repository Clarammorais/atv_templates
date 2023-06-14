from django.contrib import admin
from .models import Cursos
# Register your models here.
@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display=('nome_cursos','nome_coordenador')