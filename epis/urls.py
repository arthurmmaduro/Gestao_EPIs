from django. urls import path
from epis.views import lista_epis, cadastrar_epi, detalhes_epi, importar_excel

urlpatterns = [
    path('', lista_epis, name='lista_epis'),
    path('cadastrar/', cadastrar_epi, name='cadastrar_epi'),
    path('epis/<int:epi_id>', detalhes_epi, name='detalhes_epi'),
    path('importar/', importar_excel, name='importar_excel'),
]