# Generated by Django 2.2.14 on 2020-07-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_remove_variante_precio_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variante',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='variante',
            field=models.ManyToManyField(to='Inventario.Variante'),
        ),
    ]
