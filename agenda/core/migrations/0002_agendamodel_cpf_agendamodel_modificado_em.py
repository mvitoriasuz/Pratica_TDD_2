# Generated by Django 5.0.4 on 2024-05-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamodel',
            name='cpf',
            field=models.CharField(default='', max_length=30, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='agendamodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Modificação'),
        ),
    ]
