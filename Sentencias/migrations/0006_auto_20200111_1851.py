# Generated by Django 2.2.6 on 2020-01-12 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sentencias', '0005_auto_20200111_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentadante',
            name='salario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Salario'),
        ),
    ]