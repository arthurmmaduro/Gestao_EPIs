from django.urls import path
from colaborador.views import lista_colaborador, detalhes_colaborador, cadastrar_colaborador, editar_colaborador, exportar_realatorio_colaboradores_epis, ficha_entrega

urlpatterns = [
    path('', lista_colaborador, name='lista_colaborador'),
    path('colaboradores/<int:colaborador_id>', detalhes_colaborador, name='detalhes_colaborador'),
    path('cadastrar/', cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/<int:colaborador_id>/editar', editar_colaborador, name='editar_colaborador'),
    path('exportar_relatorio_colaboradores_epis/', exportar_realatorio_colaboradores_epis, name='exportar_relatorio_colaboradores_epis'),
    path('colaborador/<int:colaborador_id>/ficha/', ficha_entrega, name='ficha_entrega'),
]