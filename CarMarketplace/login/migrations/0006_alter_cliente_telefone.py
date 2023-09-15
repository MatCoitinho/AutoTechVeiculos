# Generated by Django 4.2.5 on 2023-09-15 19:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_remove_cliente_admin_remove_cliente_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='O número de telefone deve ter 11 dígitos (apenas números).', regex='^\\d{11}$')], verbose_name='Telefone'),
        ),
    ]
