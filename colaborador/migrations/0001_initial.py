# Generated by Django 5.1.4 on 2024-12-14 19:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('epis', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do colaborador')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('data_nascimento', models.DateField(max_length=20, verbose_name='Data de nascimento')),
                ('cargo', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('telefone', models.CharField(max_length=15)),
                ('epis', models.ManyToManyField(blank=True, related_name='colaboradores', to='epis.epi')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
