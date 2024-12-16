from django import forms
from colaborador.models import Colaborador
from epis.models import EPI

class ColaboradorForm(forms.ModelForm):
    epis = forms.ModelMultipleChoiceField(
        queryset=EPI.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False,
        label = 'EPIs Recomendados'
    )
    
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'data_nascimento', 'cargo', 'email', 'telefone', 'epis']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
    
   