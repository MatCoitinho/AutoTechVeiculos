# Generated by Django 4.2.4 on 2023-09-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunciarVeiculos', '0002_alter_anuncio_descricao_alter_anuncio_img1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='servico',
            field=models.BooleanField(default=False, verbose_name='Serviço'),
        ),
    ]
