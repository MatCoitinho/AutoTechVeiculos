# Generated by Django 4.2.5 on 2023-10-31 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitarAnuncio', '0009_alter_solicitacao_servico_alter_solicitacao_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='situacao',
            field=models.BooleanField(default=False, verbose_name='Situação'),
        ),
    ]
