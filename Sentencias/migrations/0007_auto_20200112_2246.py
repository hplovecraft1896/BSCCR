# Generated by Django 2.2.6 on 2020-01-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sentencias', '0006_auto_20200111_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentencia',
            name='fecha_inicio_juicio',
        ),
        migrations.AddField(
            model_name='sentencia',
            name='fecha_recepcion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Recepcion de Solicitud'),
        ),
    ]
