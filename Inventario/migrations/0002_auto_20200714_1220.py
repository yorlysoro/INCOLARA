# Generated by Django 2.2.14 on 2020-07-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='atributo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='valores',
        ),
        migrations.AddField(
            model_name='variante',
            name='atributo',
            field=models.ManyToManyField(related_name='VarianteAtributo', to='Inventario.Atributo'),
        ),
        migrations.AddField(
            model_name='variante',
            name='caducidad',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Caducidad'),
        ),
        migrations.AddField(
            model_name='variante',
            name='cantidad',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad a Mano'),
        ),
        migrations.AddField(
            model_name='variante',
            name='capacidad',
            field=models.PositiveIntegerField(default=0, verbose_name='Capacidad de Produccion'),
        ),
        migrations.AddField(
            model_name='variante',
            name='codigo_barras',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Codigo de Barras'),
        ),
        migrations.AddField(
            model_name='variante',
            name='coste',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Coste'),
        ),
        migrations.AddField(
            model_name='variante',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='variante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/producto/', verbose_name='Imagen del Producto'),
        ),
        migrations.AddField(
            model_name='variante',
            name='peso',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Peso'),
        ),
        migrations.AddField(
            model_name='variante',
            name='precio_extra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio Extra de Venta'),
        ),
        migrations.AddField(
            model_name='variante',
            name='volumen',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Volumen'),
        ),
        migrations.AlterField(
            model_name='atributo',
            name='valor',
            field=models.ManyToManyField(related_name='AtributoValor', to='Inventario.Valores_Atributo'),
        ),
        migrations.RemoveField(
            model_name='variante',
            name='valor',
        ),
        migrations.AddField(
            model_name='variante',
            name='valor',
            field=models.ManyToManyField(related_name='VarianteValor', to='Inventario.Valores_Atributo'),
        ),
    ]
