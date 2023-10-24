# Generated by Django 4.2.5 on 2023-10-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alugarVeiculo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alugar',
            name='data',
        ),
        migrations.RemoveField(
            model_name='alugar',
            name='horario',
        ),
        migrations.AddField(
            model_name='alugar',
            name='dataDev',
            field=models.DateField(null=True, verbose_name='Data de devolução'),
        ),
        migrations.AddField(
            model_name='alugar',
            name='dataInicio',
            field=models.DateField(null=True, verbose_name='Data da retirada'),
        ),
    ]
