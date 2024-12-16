from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from epis.models import EPI
from epis.forms import EPIForm, UploadXlsFileForm
import pandas as pd

def lista_epis(request):
    epis = EPI.objects.all().order_by('nome')
    return render(request, 'epis/lista_epis.html', {'epis': epis})

def cadastrar_epi(request):
    if request.method == 'POST':
        form = EPIForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('lista_epis')
    else:
        form = EPIForm()
        return render(request, 'epis/cadastrar_epi.html', {'form': form})
    
def detalhes_epi(request, epi_id):
    epi = get_object_or_404(EPI, pk=epi_id)
    return render(request, 'epis/detalhes_epi.html', {'epi': epi})

def importar_excel(request):
    if request.method == 'POST':
        form = UploadXlsFileForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            try:
                df = pd.read_excel(arquivo)

                df = df.dropna(how='all')

                for _,row in df.iterrows():
                    EPI.objects.create(
                        nome = row['EPI'],
                        modelo = row['Modelo'],
                        fabricante = row['Fabricante'],
                        descricao = row['Característica'],
                        numero_ca = row['CA da Etiqueta'],
                        validade_ca = row['Validade do CA'],
                    )
                messages.success(request, 'Dados importados com sucesso!')
                return redirect('lista_epis')
            
            except Exception as e:
                messages.error(request, f'Erro ao processar o arquivo: {str(e)}')
                return redirect('lista_epis')
    else:
        form = UploadXlsFileForm  

        return render(request, 'epis/importar_excel.html', {'form': form})  
