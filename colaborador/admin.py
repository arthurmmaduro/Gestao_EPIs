from django.contrib import admin
from colaborador.models import Colaborador
from colaborador.forms import ColaboradorForm

# Register your models here.

class ListandoColaboradores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento', 'email', 'telefone')
    list_display_links = ('id', 'nome')

class ColaboradorAdmin(admin.ModelAdmin):
    form = ColaboradorForm

admin.site.register(Colaborador, ColaboradorAdmin)
