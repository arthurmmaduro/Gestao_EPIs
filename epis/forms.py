from django import forms
from epis.models import EPI

class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'modelo', 'fabricante' , 'descricao', 'numero_ca', 'arquivo_ca', 'validade_ca', 'categoria']

    def clean_validade_ca(self):
        validade_ca = self.cleaned_data.get('validade_ca')
        if validade_ca == "":
            return None
        return validade_ca

class UploadXlsFileForm(forms.Form):
    arquivo = forms.FileField(label='Selecionar um arquivo Excel')