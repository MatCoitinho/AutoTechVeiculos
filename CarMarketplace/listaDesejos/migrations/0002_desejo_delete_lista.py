# Generated by Django 4.2.5 on 2023-12-04 21:58

from django.db import migrations, models
import django.db.models.deletion
import listaDesejos.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_remove_cliente_lista'),
        ('listaDesejos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desejo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('ano', models.IntegerField(help_text='O ano deve ter no máximo 4 dígitos', validators=[listaDesejos.models.validar_data], verbose_name='Ano')),
                ('dono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.cliente', verbose_name='Dono')),
            ],
        ),
        migrations.DeleteModel(
            name='Lista',
        ),
    ]
