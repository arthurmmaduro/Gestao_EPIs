from django.shortcuts import render ,redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from autenticacao.forms  import CustomUserCreationForm
from colaborador.forms import ColaboradorForm   

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'autenticacao/login.html'