# Generated by Django 5.1.4 on 2024-12-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('modelo', models.CharField(default='', max_length=200)),
                ('fabricante', models.CharField(blank=True, max_length=200, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('numero_ca', models.CharField(max_length=10)),
                ('arquivo_ca', models.FileField(blank=True, null=True, upload_to='ca_pdfs/')),
                ('validade_ca', models.DateField(blank=True, null=True)),
                ('categoria', models.CharField(choices=[('respiratória', 'Proteção Respiratória'), ('visual', 'Proteção para os Olhos'), ('cabeça', 'Proteção para a Cabeça'), ('auditiva', 'Proteção Auditiva'), ('mãos', 'Proteção para as Mãos'), ('pés', 'Proteção para os Pés'), ('química', 'Proteção contra Produtos Químicos'), ('tronco', 'Proteção para o Tronco'), ('quedas', 'Proteção contra Quedas de Diferentes Níveis')], default='', max_length=50)),
            ],
        ),
    ]
