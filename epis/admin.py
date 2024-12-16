from django.contrib import admin
from epis.models import EPI

# Register your models here.

class ListandoEPIs(admin.ModelAdmin):
    list_display = ('id', 'nome', 'modelo', 'fabricante' , 'descricao', 'numero_ca', 'validade_ca', 'categoria')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'numero_ca')
    # list_filter = ('categoria',)

admin.site.register(EPI, ListandoEPIs)