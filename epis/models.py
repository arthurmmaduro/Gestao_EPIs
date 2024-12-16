from django.db import models

# Create your models here.
OPCOES_CATEGORIA = [
    ('respiratória', 'Proteção Respiratória'),
    ('visual', 'Proteção para os Olhos'),
    ('cabeça', 'Proteção para a Cabeça'),
    ('auditiva', 'Proteção Auditiva'),
    ('mãos', 'Proteção para as Mãos'),
    ('pés', 'Proteção para os Pés'),
    ('química', 'Proteção contra Produtos Químicos'),
    ('tronco', 'Proteção para o Tronco'),
    ('quedas', 'Proteção contra Quedas de Diferentes Níveis'),
]

class EPI(models.Model):
    nome = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200, default='')
    fabricante = models.CharField(max_length=200, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    numero_ca = models.CharField(max_length=10)
    arquivo_ca = models.FileField(upload_to='ca_pdfs/', blank=True, null=True)
    validade_ca = models.DateField(null=True, blank=True)
    categoria = models.CharField(max_length=50, choices = OPCOES_CATEGORIA, default='')
    

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.validade_ca == "":  # Corrigir valores inválidos
            self.validade_ca = None
        super().save(*args, **kwargs)
