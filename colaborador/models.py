from django.db import models
from django.conf import settings
from epis.models import EPI

# Create your models here.

class Colaborador(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, verbose_name='Nome do colaborador')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    data_nascimento = models.DateField(max_length=20, verbose_name='Data de nascimento')
    cargo = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    telefone = models.CharField(max_length=15)
    epis = models.ManyToManyField(EPI, blank=True, related_name='colaboradores')

        
    def __str__(self):
        return self.usuario.email
   