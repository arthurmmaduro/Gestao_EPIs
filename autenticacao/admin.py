from django.contrib import admin
from autenticacao.models import CustomUser
from colaborador.models import Colaborador

# Register your models here.


# # Preencher valores de usuário para colaboradores existentes
# for colaborador in Colaborador.objects.filter(usuario__isnull=True):
#     # Substitua 'email@example.com' por dados reais ou crie usuários conforme necessário
#     user = CustomUser.objects.create(email=f'{colaborador.cpf}@example.com', password='defaultpassword')
#     colaborador.usuario = user
#     colaborador.save()
